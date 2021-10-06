use std::time::Instant;

fn part1(a: &u64, b: &u64) -> u32 {
    let mut gen_a = *a;
    let mut gen_b = *b;
    let mut res = 0;

    for _ in 0..40_000_000 {
        gen_a = gen_a * 16807 % 2147483647;
        gen_b = gen_b * 48271 % 2147483647;
        if gen_a & 0xffff == gen_b & 0xffff {
            res += 1;
        }
    }
    res
}

fn part2(a: &u64, b: &u64) -> u32 {
    let mut gen_a = *a;
    let mut gen_b = *b;
    let mut res = 0;

    for _ in 0..5_000_000 {
        loop {
            gen_a = gen_a * 16807 % 2147483647;
            if gen_a % 4 == 0 { break; }
        }
        loop {
            gen_b = gen_b * 48271 % 2147483647;
            if gen_b % 8 == 0 { break; }
        }
        if gen_a & 0xffff == gen_b & 0xffff {
            res += 1;
        }
    }
    res
}

fn main() {
    let start = Instant::now();
    let gen_a: u64 = 873;
    let gen_b: u64 = 583;

    println!("Part 1: {}", part1(&gen_a, &gen_b));
    println!("Part 2: {}", part2(&gen_a, &gen_b));
    
    let el = &start.elapsed();
    println!("Time: {}.{} s", el.as_secs(), el.subsec_millis());
}
