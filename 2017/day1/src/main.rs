use std::fs;

pub fn string_to_int_vec(s: &str) -> Vec<u32> {
    s.chars().map(|c| c.to_digit(10).unwrap()).collect()
}

fn sum_with_distance(nums: &Vec<u32>, dist: usize) -> u32 {
    let mut sum = 0;
    for i in 0..nums.len() {
        let ni = (i + dist) % nums.len();
        if nums[i] == nums[ni] {
            sum += nums[i];
        }
    }
    sum
}

fn main() {
    let data: String = fs::read_to_string("src/input.txt").unwrap();
    let nums: Vec<u32> = string_to_int_vec(&data);
    let half_dist = nums.len() / 2;

    println!("Part 1: {}", sum_with_distance(&nums, 1));
    println!("Part 2: {}", sum_with_distance(&nums, half_dist));
}
