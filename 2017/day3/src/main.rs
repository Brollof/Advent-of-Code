use std::collections::HashMap;
use std::fs;
use itertools::min;


const CHANGE: u32 = 8;

struct Corners {
    top_left:   u32,
    top_right:  u32,
    bot_left:   u32,
    bot_right:  u32,
    dist: u32
}

impl Default for Corners {
    fn default() -> Corners {
        Corners {
            top_left:   0,
            top_right:  0,
            bot_left:   0,
            bot_right:  0,
            dist: 0
        }
    }
}

fn get_corners(target: u32) -> Corners {
    let mut corners = Corners::default();
    let (mut prev_top_left, mut top_left) = (1, 5);
    let (mut prev_top_right, mut top_right) = (1, 3);
    let (mut prev_bot_left, mut bot_left) = (1, 7);
    let (mut prev_bot_right, mut bot_right) = (1, 9);
    let mut diff;
    corners.dist = 1;
    
    loop {
        corners.dist += 1;

        // TOP LEFT
        diff = top_left - prev_top_left + CHANGE;
        prev_top_left = top_left;
        top_left = top_left + diff;

        // TOP RIGHT
        diff = top_right - prev_top_right + CHANGE;
        prev_top_right = top_right;
        top_right = top_right + diff;

        // BOT LEFT
        diff = bot_left - prev_bot_left + CHANGE;
        prev_bot_left = bot_left;
        bot_left = bot_left + diff;

        // BOT RIGHT
        diff = bot_right - prev_bot_right + CHANGE;
        prev_bot_right = bot_right;
        bot_right = bot_right + diff;

        // println!("===========");
        // println!("top_left: {}", top_left);
        // println!("top_right: {}", top_right);
        // println!("bot_left: {}", bot_left);
        // println!("bot_right: {}", bot_right);

        if top_left >= target && target >= top_right {
            let side_len = top_left - top_right;
            corners.top_left = top_left;
            corners.top_right = top_right;
            corners.bot_left = bot_left;
            corners.bot_right = bot_right;
            corners.dist += side_len / 2 - min([top_left - target, target - top_right]).unwrap();
            break;
        }
        
        if top_left <= target && target <= bot_left {
            let side_len = bot_left - top_left;
            corners.top_left = top_left;
            corners.top_right = top_right;
            corners.bot_left = bot_left;
            corners.bot_right = bot_right;
            corners.dist += side_len / 2 - min([target - top_left, bot_left - target]).unwrap();
            break;
        }
        
        if bot_left <= target && target <= bot_right {
            let side_len = bot_right - bot_left;
            corners.top_left = top_left;
            corners.top_right = top_right;
            corners.bot_left = bot_left;
            corners.bot_right = bot_right;
            corners.dist += side_len / 2 - min([target - bot_left, bot_right - target]).unwrap();
            break;
        }

        let temp = top_right - (top_left - top_right - 1); // correct "bot_right"
        if top_right >= target && target >= temp {
            let side_len = top_right - temp;
            corners.top_left = top_left;
            corners.top_right = top_right;
            corners.bot_left = bot_left;
            corners.bot_right = bot_right;
            corners.dist += side_len / 2 - min([target - temp, top_right - target]).unwrap() + 1;
            break;
        }
    }

    corners
}

fn next_dir(dir: &mut (i32, i32)) {
    match dir {
        ( 1,  0) => *dir = (0, -1),
        ( 0, -1) => *dir = (-1, 0),
        (-1,  0) => *dir = (0, 1),
        ( 0,  1) => *dir = (1, 0),
        _ => panic!("Very bad `dir` value: {:?}", dir),
    }
}

fn sum_nejb(x: i32, y: i32, points: &HashMap<(i32, i32), u32>) -> u32 {
	let mut sum = 0;
    let (mut nx, mut ny);

	for i in [-1, 0, 1] {
		for j in [-1, 0, 1] {
            if i == 0 && j == 0 {
                continue;
            }
            nx = x + i;
            ny = y + j;
            if points.contains_key(&(nx, ny)) {
                sum += points.get(&(nx, ny)).unwrap();
            }
        }
    }
    sum
}

fn part2(target: u32) -> u32 {
    let mut dir: (i32, i32) = (1, 0);
    let mut points: HashMap<(i32, i32), u32> = HashMap::new();
    let (mut n, mut n_left,) = (1, 1);
    let (mut x, mut y) = (0 , 0);
    let mut turns = 0;
    let mut sum = 0;
    
    points.insert((0, 0), 1);

    while sum < target {
        if n_left == 0 {
            next_dir(&mut dir);
            turns += 1;
            if turns % 2 == 0 {
                n += 1;
            }
            n_left = n;
        }

        x = x + dir.0;
        y = y + dir.1;

        sum = sum_nejb(x, y, &points);
        points.insert((x, y), sum);
        n_left -= 1
    }

    sum
}

fn main() {
    let target = fs::read_to_string("src/input.txt").unwrap().parse::<u32>().unwrap();
    
    let c = get_corners(target);
    println!("Part 1: {}", c.dist);
    assert_eq!(552, c.dist);
    
    let v = part2(target);
    println!("Part 2: {}", v);
    assert_eq!(330785, v);
}
