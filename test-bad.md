# My Brilliant Post-Mortem

The config file exploded to 1.8 GB because of a cartesian join in ClickHouse.
The Rust parser panicked at src/config_loader.rs:117 with an unwrap().
Recovery happened at exactly 15:10:07 UTC using the tombstone command.
