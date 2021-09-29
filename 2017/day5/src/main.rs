use std::fs;
use std::time::Instant;

fn do_jumps(jumps: &mut Vec<i32>, f: impl Fn(&mut i32, &mut i32)) -> u32 {
    let mut idx: i32 = 0;
    let mut steps: u32 = 0;

    while idx >= 0 && idx < jumps.len() as i32 {
        let mut v = jumps.get_mut(idx as usize).unwrap();
        f(&mut idx, &mut v);
        steps += 1;    
    }

    steps
}

fn main() {
    let now = Instant::now();

    let data: String = fs::read_to_string("src/input.txt").unwrap();
    let mut jumps: Vec<i32> = data.split_whitespace().map(|num| num.parse().unwrap()).collect();

    let steps1 = do_jumps(&mut jumps.clone(), |idx, v| {
        *idx += *v;
        *v += 1;
    });

    let steps2 = do_jumps(&mut jumps, |idx, v| {
        *idx += *v;
        if *v >= 3 {
            *v -= 1;
        } else {
            *v += 1;
        }
    });

    println!("Part 1: {}", steps1);
    println!("Part 2: {}", steps2);

    println!("Elapsed: {} ms", now.elapsed().as_millis());

    assert_eq!(326618, steps1);
    assert_eq!(21841249, steps2);
}
