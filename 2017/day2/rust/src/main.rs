use std::fs;
use itertools::Itertools;

fn main() {
    let data: String = fs::read_to_string("src/input.txt").unwrap();
    let (mut c1, mut c2) = (0, 0);

    for line in data.lines() {
        let nums: Vec<i32> = line.split_whitespace().map(|n| n.parse::<i32>().unwrap()).collect();

        // part 1 calculations
        let (min, max) = nums.iter().minmax().into_option().unwrap();
        c1 += max - min;

        // part 2 calculations
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] % nums[j] == 0 {
                    c2 += nums[i] / nums[j];
                } else if nums[j] % nums[i] == 0 {
                    c2 += nums[j] / nums[i];
                }
            }
        }
    }

    println!("Part 1: {}", c1);
    assert_eq!(46402, c1);

    println!("Part 2: {}", c2);
    assert_eq!(265, c2);
}
