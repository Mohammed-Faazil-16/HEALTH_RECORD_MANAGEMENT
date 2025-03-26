from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import HealthRecord, Patient
from .serializers import HealthRecordSerializer
from .blockchain import add_record, get_records


class AddHealthRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        try:
            patient = Patient.objects.get(user=request.user)
            tx_hash = add_record(
                patient_id=data["patient_id"],
                doctor_id=data["doctor_id"],
                diagnosis=data["diagnosis"],
                prescription=data["prescription"],
                record_hash=data["record_hash"],
                sender_address=patient.eth_address
            )
            health_record = HealthRecord.objects.create(
                patient=patient,
                doctor_id=data["doctor_id"],  # Now correct
                record_hash=tx_hash
            )
            serializer = HealthRecordSerializer(health_record)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        except KeyError as e:
            return Response({"error": f"Missing field: {e}"}, status=400)
        except Exception as e:
            return Response({"error": f"Server error: {str(e)}"}, status=500)
        
class GetHealthRecordsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patient = Patient.objects.get(user=request.user)
        records = get_records(patient.eth_address)
        return Response({"records": records})