use std::fs;
use std::collections::HashMap;
use itertools::Itertools;

fn is_valid(words: &Vec<String>) -> bool {
    let mut counter: HashMap<String, u32> = HashMap::new();

    for word in words {
        *counter.entry(word.to_string()).or_insert(0) += 1;
    }

    if counter.values().all(|v| *v == 1) {
        return true;
    }
    false
}

fn main() {
    let data: String = fs::read_to_string("src/input.txt").unwrap();
    let mut valids1 = 0;
    let mut valids2 = 0;
    
    for line in data.lines() {
        let words1: Vec<String> = line.split_whitespace().map(String::from).collect();
        let words2: Vec<String> = line.split_whitespace().map(|word| word.chars().sorted().collect::<String>()).collect();

        valids1 += is_valid(&words1) as u32;
        valids2 += is_valid(&words2) as u32;

    }

    println!("Part 1: {}", valids1);
    println!("Part 2: {}", valids2);

    assert_eq!(466, valids1);
    assert_eq!(251, valids2);
}
