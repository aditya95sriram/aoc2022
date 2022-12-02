use std::io;

fn main() {
    let mut p1_total = 0;
    let mut p2_total = 0;
    const A_X_OFFSET: i32 = 23;
    const POINTS_OFFSET: i32 = 64;

    loop {
        let mut line = String::new();
        match io::stdin().read_line(&mut line) {
            Ok(num) => {
                if num == 0 {
                    break;
                }
            }
            Err(_) => println!("error reading line"),
        }

        let round: Vec<&str> = line.split(' ').collect();
        let opp = round[0].as_bytes()[0] as i32;
        let me = round[1].as_bytes()[0] as i32 - A_X_OFFSET;

        // [part 1] X, Y, Z denotes rock, paper, scissors
        // add 1 for rock, 2 for paper, 3 for scissors
        p1_total += me - POINTS_OFFSET;

        p1_total += if opp == me {
            3
        } else if (opp % 3) == ((me - 1) % 3) {
            6
        } else {
            0
        };

        // [part 2] X, Y, Z denotes win, lose, draw
        // result = 0/1/2 for win/loss/draw
        let result = me - POINTS_OFFSET - 1;
        p2_total += result * 3;

        // map opponent's move to 0,1,2 (rock, paper, scissors)
        let opp = opp - POINTS_OFFSET - 1;
        
        // find our move using opponent's move and result
        // (using rem_euclid instead of plain `%` to handle -ve numbers)
        // [stackoverflow/q/31210357]
        let me = (opp + result - 1).rem_euclid(3);

        // add 1 for rock, 2 for paper, 3 for scissors
        p2_total += me + 1;
    }

    println!("{p1_total} {p2_total}");
}
