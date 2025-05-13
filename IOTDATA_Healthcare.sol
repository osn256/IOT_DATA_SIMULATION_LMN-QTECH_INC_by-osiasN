//------------------MO-IT148 Homework: WEEK 3 IoT Data STORAGE_A3101_NIEVA OSIAS JR--------------------
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;                         
contract IoTHealthcare {                        // Contract name
    address public owner;                       // Owner of the contract

    constructor() {                             // Constructor function
        owner = msg.sender;                     // Set the contract deployer as the owner
    }

    modifier onlyOwner() {                      // Modifier to restrict access to owner
        require(msg.sender == owner, "Access denied");  // Check if the sender is the owner
        _;
    }

    struct BasicInfo {                          // Structure for basic patient information
        string name;                            // Patient's name   
        string birthDate;                       // Patient's birth date  
        uint256 age;                            // Patient's age    
        uint256 timestamp;                      // Timestamp of record creation 
    }

    struct Vitals {                             // Structure for patient vitals      
        uint8 heartRate;                        // Heart rate  
        uint8 systolic;                         // Systolic blood pressure    
        uint8 diastolic;                        // Diastolic blood pressure    
        uint8 oxygenLevel;                      // Oxygen saturation level   
    }

    struct Activity {                           // Structure for patient activity data      
        uint256 stepsCount;                     // Number of steps taken  
        string activityLevel;                   // Activity level (e.g., low, moderate, high)
        string sleepQuality;                    // Sleep quality (e.g., good, fair, poor)
        string location;                        // Location of activity (e.g., home, gym, outdoors)
    }

    mapping(string => BasicInfo) private basicInfos;        // Mapping to store basic information of patients
    mapping(string => Vitals) private vitalsData;           // Mapping to store vitals data of patients
    mapping(string => Activity) private activityData;       // Mapping to store activity data of patients

    string[] private patientIds;                            // Array to store patient IDs   

    event RecordAdded(string patientId, uint256 timestamp); // Event to log when a record is added

    function addBasicInfo(                      // Function to add basic information of a patient
        string memory patientId,                // Patient ID
        string memory name,                     // Patient's name  
        string memory birthDate,                // Patient's birth date
        uint256 age                             // Patient's age 
    ) public onlyOwner {                        // Only owner can add basic info
        basicInfos[patientId] = BasicInfo(name, birthDate, age, block.timestamp);   // Store basic info in mapping
        patientIds.push(patientId);                         // Add patient ID to the array
        emit RecordAdded(patientId, block.timestamp);       // Emit event to log record addition
    }

    function addVitals(                         // Function to add vitals data of a patient 
        string memory patientId,                // Patient ID
        uint8 heartRate,                        // Heart rate  
        uint8 systolic,                         // Systolic blood pressure   
        uint8 diastolic,                        // Diastolic blood pressure 
        uint8 oxygenLevel                       // Oxygen saturation level   
    ) public onlyOwner {                        // Only owner can add vitals data       
        vitalsData[patientId] = Vitals(heartRate, systolic, diastolic, oxygenLevel);        // Store vitals data in mapping
    }

    function addActivity(                       // Function to add activity data of a patient
        string memory patientId,                // Patient ID
        uint256 stepsCount,                     // Number of steps taken  
        string memory activityLevel,            // Activity level (e.g., low, moderate, high)  
        string memory sleepQuality,             // Sleep quality (e.g., good, fair, poor)
        string memory location                  // Location of activity (e.g., home, gym, outdoors)
    ) public onlyOwner {                        // Only owner can add activity data 
        activityData[patientId] = Activity(stepsCount, activityLevel, sleepQuality, location);  // Store activity data in mapping
    }

    function getBasicInfo(string memory patientId) public view returns (        // Function to get basic information of a patient
        string memory name,                 // Patient's name   
        string memory birthDate,            // Patient's birth date               
        uint256 age,                        // Patient's age
        uint256 timestamp                   // Timestamp of record creation
    ) {
        BasicInfo memory b = basicInfos[patientId];         // Retrieve basic info from mapping
        return (b.name, b.birthDate, b.age, b.timestamp);   // Return basic info
    }

    function getVitals(string memory patientId) public view returns (       // Function to get vitals data of a patient
        uint8 heartRate,            // Heart rate
        uint8 systolic,             // Systolic blood pressure
        uint8 diastolic,            // Diastolic blood pressure   
        uint8 oxygenLevel           // Oxygen saturation level
    ) {
        Vitals memory v = vitalsData[patientId];                        // Retrieve vitals data from mapping        
        return (v.heartRate, v.systolic, v.diastolic, v.oxygenLevel);   // Return vitals data
    }

    function getActivity(string memory patientId) public view returns ( // Function to get activity data of a patient
        uint256 stepsCount,                                             // Number of steps taken        
        string memory activityLevel,                                    // Activity level (e.g., low, moderate, high)
        string memory sleepQuality,                                     // Sleep quality (e.g., good, fair, poor)
        string memory location                                          // Location of activity (e.g., home, gym, outdoors) 
    ) {
        Activity memory a = activityData[patientId];                    // Retrieve activity data from mapping
        return (a.stepsCount, a.activityLevel, a.sleepQuality, a.location); // Return activity data
    }

    function getAllPatientIds() public view returns (string[] memory) { // Function to get all patient IDs
        return patientIds;                                              // Return array of patient IDs      
    }
}
