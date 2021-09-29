use std::fs;
use itertools::max;
use std::time::Instant;
use std::collections::HashMap;

fn main() {
    let now = Instant::now();

    let data: String = fs::read_to_string("src/input.txt").unwrap();
    let mut banks: Vec<u32> = data.split_whitespace().map(|num| num.parse().unwrap()).collect();
    let mut states_cycles: HashMap<Vec<u32>, u32> = HashMap::new();
    let mut cycles: u32 = 0;

    states_cycles.insert(banks.clone(), 0);

    loop {
        let mut blocks: u32 = *max(&banks).unwrap();
        let mut idx = banks.iter().position(|&v| v == blocks).unwrap();
        
        cycles += 1;
        banks[idx] = 0;

        // Redistributate blocks
        while blocks > 0 {
            idx = (idx + 1) % banks.len();
            banks[idx] += 1;
            blocks -= 1;
        }

        // Check if state was seen before
        if states_cycles.contains_key(&banks) {
            break;
        }

        states_cycles.insert(banks.clone(), cycles);
    }

    let loop_size = cycles - states_cycles[&banks];

    println!("State seen before: {:?}", banks);
    println!("Cycles: {}", cycles);
    println!("Loop size: {}", loop_size);

    assert_eq!(14029, cycles);
    assert_eq!(2765, loop_size);

    let el = now.elapsed();
    println!("Done in {}.{}s", el.as_secs(), el.subsec_millis());
}
