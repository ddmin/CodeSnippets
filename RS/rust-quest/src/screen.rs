use std::fmt;
use std::io::{stdin, stdout, Write};

// Read user input
pub fn read(input: &mut String) {
    stdout().flush()
        .expect("faled to flush");
    stdin().read_line(input)
        .expect("failed to read");
}

// Pause dialogue
pub fn pause() {
    let mut nothing = String::new();
    print!("== Press Enter to Continue ==");
    read(&mut nothing);
}

// Clear screen
pub fn clear() {
    print!("{}[2J", 27 as char);
}
