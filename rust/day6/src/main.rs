use std::io;
use std::collections::HashSet;

const N: usize = 4;  // set N to 14 for part 2

fn all_different(slice: &str) -> bool {
    let mut set = HashSet::new();
    for c in slice.chars() {
        set.insert(c);
    }
    return set.len() == slice.len();
}

fn main() {
    let mut line = String::new();
    io::stdin()
        .read_line(&mut line)
        .expect("failed to read line");
    for i in 0..line.len()-N+1 {
        if all_different(&line[i..i+N]) {
            println!("{}", i + N);
            break
        }
    }
}
