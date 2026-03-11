# TODOs
In this document, all the TODOs are listed for foture development and adjustements.

## emendo
### errors.py
- [ ] Create `errors` module:
    - [ ] Add emendo errors in order to limit usage of mixed exceptions 

### noises
- [ ] `Noise` implementations:
    - [ ] Add multi-channel noise generation by passing a shape
    - [ ] Refactor

- [ ] `NoiseConfig`:
    - [ ] Create serializer to dictionary
    - [ ] Create deserializer from dictionary

- [ ] Add `MagneticNoise`:
    - [ ] Add soft-iron deformation
    - [ ] Add hard-iron deformation

### sensors
- [ ] `Sensors`:
    - [ ] Add noise to data
    - [ ] Add noise to data

- [ ] `SensorsConfig`:
    - [ ] Add deserialization from file
    - [ ] Add independent sensors noises:
        - [ ] Add `accelerometer_noise`
        - [ ] Add `gyroscope_noise`
        - [ ] Add `magnetometer_noise`


#### generators
- [ ] `KinameticGenerator` implementations:
    - [ ] Switch to timestamp generation (no `start`, `stop`, `freq` parameters)
    - [ ] Add check for max_duration (timestamp must not exceed max_duration)
    - [ ] Refactor

- [ ] `AttitudeGenerator` implementations:
    - [ ] Switch to timestamp generation (no `start`, `stop`, `freq` parameters)
    - [ ] Add check for max_duration (timestamp must not exceed max_duration)
    - [ ] Refactor

- [ ] `MagneticGenerator` implementations:
    - [ ] Add out-of-bound check for position
    - [ ] Refactor

- [ ] `GeneratorConfig`:
    - [ ] Create serializer to dictionary
    - [ ] Create deserializer from dictionary
    - [ ] Refactor

---