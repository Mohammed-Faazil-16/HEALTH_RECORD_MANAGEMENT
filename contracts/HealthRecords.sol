// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HealthRecords {
    // Structure to hold a single health record
    struct Record {
        string patientId;        // Unique ID for the patient
        string doctorId;         // ID of the doctor who created the record
        string diagnosis;        // Diagnosis or medical condition
        string prescription;     // Prescribed medications or treatments
        string recordHash;       // Hash of the record document (e.g., IPFS hash)
        uint256 timestamp;       // Timestamp of when the record was created
    }

    // Patient's address to their health records
    mapping(address => Record[]) private records;

    // Event to log whenever a new health record is added
    event RecordAdded(
        address indexed patientAddress,
        string patientId,
        string doctorId,
        uint256 timestamp
    );

    // Modifier to ensure valid inputs
    modifier validString(string memory str) {
        require(bytes(str).length > 0, "Input string cannot be empty");
        _;
    }

    // Add a health record for the sender (patient)
    function addRecord(
        string memory _patientId,
        string memory _doctorId,
        string memory _diagnosis,
        string memory _prescription,
        string memory _recordHash
    ) public validString(_patientId) validString(_doctorId) validString(_recordHash) {
        Record memory newRecord = Record({
            patientId: _patientId,
            doctorId: _doctorId,
            diagnosis: _diagnosis,
            prescription: _prescription,
            recordHash: _recordHash,
            timestamp: block.timestamp
        });
        records[msg.sender].push(newRecord);

        // Emit an event for the added record
        emit RecordAdded(msg.sender, _patientId, _doctorId, block.timestamp);
    }

    // Retrieve all health records of the sender
    function getMyRecords() public view returns (Record[] memory) {
        return records[msg.sender];
    }

    // Retrieve health records of a specific patient (only callable by the patient)
    function getRecordsByPatient(address _patientAddress) public view returns (Record[] memory) {
        require(msg.sender == _patientAddress, "Access denied: Only the patient can view their records");
        return records[_patientAddress];
    }

    // Count the number of records a patient has
    function getRecordCount() public view returns (uint256) {
        return records[msg.sender].length;
    }
}
