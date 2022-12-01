use std::io;

fn main() {
    // haven't yet learned to use vectors
    const MAXELFS: usize = 1000;
    let mut elfs = [0; MAXELFS];
    let mut current_elf = 0;

    // read in total calories per elf
    loop {
        let mut line = String::new();
        match io::stdin()
                .read_line(&mut line) {
                    // Ok with 0 bytes read means EOF
                    Ok(num) => if num == 0 {break;},
                    Err(_)  => println!("error reading line"),
                }
        
        match line.trim().parse::<i32>() {
            Ok(cal) => elfs[current_elf] += cal,
            Err(_) => current_elf += 1, 
        }
    }

    // [part 1] compute max calories (part 1)
    // let maxcal = elfs.into_iter().reduce(i32::max).unwrap();

    // [part 2] compute total of top 3 elves
    elfs.sort();
    elfs.reverse();
    let maxcal = elfs[0] + elfs[1] + elfs[2];

    println!("{maxcal}");
}
