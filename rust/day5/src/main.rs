use std::io;

fn main() {
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut stacking = true;

    loop {
        let mut line = String::new();
        match io::stdin().read_line(&mut line) {
            Err(_) => println!("failed to read line"),
            Ok(num) => {
                if num == 0 {
                    // end of file
                    break;
                } else {
                    if stacking {
                        if stacks.len() == 0 {
                            // init stacks
                            let numstacks = (line.len() + 1) / 4;
                            for _ in 0..numstacks {
                                stacks.push(Vec::new());
                            }
                        }
                        // push onto stacks
                        if !line.trim().starts_with('[') {
                            stacking = false;
                            continue;
                        }
                        let mut stack_idx = 0;
                        for crate_name in line.chars().skip(1).step_by(4) {
                            if crate_name != ' ' {
                                stacks[stack_idx].insert(0, crate_name);
                            }
                            stack_idx += 1;
                        }
                    } else {
                        if line.trim().len() == 0 {
                            continue;
                        }
                        let comps: Vec<&str> = line
                            .split_whitespace()
                            .skip(1)
                            .step_by(2)
                            .collect();
                        let count: usize = comps[0].parse().unwrap();
                        let src: usize = comps[1].parse().unwrap();
                        let dest: usize = comps[2].parse().unwrap();

                        // [part 1] transfer in reverse order
                        // for _ in 0..count {
                        //     let transfer = stacks[src-1].pop().unwrap();
                        //     stacks[dest-1].push(transfer);
                        // }

                        // [part 2] transfer in same order
                        // below code would've been nice but doesn't work
                        // let transfer = stacks[src-1].iter().rev().take(count).rev().collect();
                        // stacks[dest-1].extend(transfer);
                        let mut transfer: Vec<char> = Vec::new();
                        for _ in 0..count {
                            transfer.push(stacks[src-1].pop().unwrap());
                        }
                        for _ in 0..count {
                            stacks[dest-1].push(transfer.pop().unwrap());
                        }
                    }
                }
            },
        }
    }

    // print tops of stacks
    for stack in stacks {
        print!("{}", stack.last().unwrap());
    }
    print!("\n");
}
