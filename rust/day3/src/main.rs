use std::io;

// don't fully understand borrowing yet
// used compiler assistance for now
fn intersect(s1: &str, s2: &str) -> Vec<u8> {
    let mut result = Vec::new();
    for byte1 in s1.bytes() {
        for byte2 in s2.bytes() {
            if byte1 == byte2 {
                result.push(byte1);
            }
        }
    }
    result
}

fn priority(c: u8) -> u8 {
    if c > b'Z' {  // a-z
        c - b'a' + 1
    } else {  // A-Z
        c - b'A' + 27
    }
}

fn main() {
    let mut sacks: Vec<String> = Vec::new();

    loop {
        let mut sack = String::new();
        match io::stdin().read_line(&mut sack) {
            Ok(num) => {
                if num == 0 {
                    break;
                } else {
                    sacks.push(sack);
                }
            }
            Err(_) => println!("error reading line"),
        }
    }

    // [part 1] add priorities of item common in both compartments
    let mut p1_total = 0;
    for sack in &sacks {
        let (left, right) = sack.split_at(sack.len() / 2);
        let common = intersect(left, right)[0];
        p1_total += priority(common) as i32;
    }

    // [part 2] add priorities of common badge in sets of 3
    let mut p2_total = 0;
    for i in (0..sacks.len()).step_by(3) {
        let common = intersect(&sacks[i], &sacks[i + 1]);
        let common = intersect(
            &std::str::from_utf8(&common).unwrap(), 
            &sacks[i + 2]
        );
        p2_total += priority(common[0]) as i32;
    }
    println!("{p1_total} {p2_total}");
}
