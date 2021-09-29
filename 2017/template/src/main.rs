use std::fs;

fn main() {
    let data: String = fs::read_to_string("src/input.txt").unwrap();

    println!("{}", data);
}
