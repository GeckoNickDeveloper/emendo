# TODOs
In this document, all the TODOs are listed for future development and adjustements.

## emendo
### errors.py
- [ ] Create `errors` module:
    - [ ] Add emendo errors in order to limit usage of mixed exceptions 

### noises
- [x] `Noise` implementations:
    - [x] Add multi-channel noise generation by passing a shape
    - [x] Refactor

- [ ] `NoiseConfig`:
    - [ ] Create serializer to dictionary
    - [ ] Create deserializer from dictionary
    - [x] Remove frequency

- [ ] Add `MagneticBias`:
    - [ ] Add soft-iron deformation
    - [ ] Add hard-iron deformation

### sensors
- [ ] `Sensors`:
    - [ ] Add different noise generators
    - [x] Add noise to data
    - [x] Add anti-aliasing filter

- [ ] `SensorsConfig`:
    - [ ] Add deserialization from file
    - [ ] Add independent sensors noises:
        - [ ] Add `accelerometer_noise`
        - [ ] Add `gyroscope_noise`
        - [ ] Add `magnetometer_noise`


#### generators
- [ ] `KinameticGenerator` implementations:
    - [x] Switch to timestamp generation (no `start`, `stop`, `freq` parameters)
    - [x] Add check for max_duration (timestamp must not exceed max_duration)
    - [ ] Refactor

- [ ] `AttitudeGenerator` implementations:
    - [x] Switch to timestamp generation (no `start`, `stop`, `freq` parameters)
    - [x] Add check for max_duration (timestamp must not exceed max_duration)
    - [ ] Refactor

- [ ] `MagneticGenerator` implementations:
    - [x] Add out-of-bound check for position
    - [ ] Refactor

- [ ] `GeneratorConfig`:
    - [ ] Create serializer to dictionary
    - [ ] Create deserializer from dictionary
    - [ ] Refactor

---