use std::fs;

#[derive(Debug, Clone)]
struct TreeNode {
    name: String,
    weight: u32,
    parent: Option<Box<TreeNode>>,
    level: u32,
    children: Vec<TreeNode>
}

impl TreeNode {
    fn new(name: &str, weight: u32) -> TreeNode {
        TreeNode {
            name: name.to_string(),
            weight: weight,
            parent: None,
            level: 0,
            children: Vec::new()
        }
    }
    fn add_child(&mut self, child: TreeNode) {
        self.children.push(child);
    }

    fn get_level(&self) -> u32 {
        let mut level = 0;
        let mut p = self.parent.as_ref();
        while p.is_some() {
            level += 1;
            let new_p = p.unwrap().as_ref();
            p = new_p.parent.as_ref();
        }
        level
    }

    fn print_tree(&self) {
        let level = self.get_level();
        let prefix = "   ".repeat(level as usize);
        println!("{}|__{}", prefix, self.name);
        for child in self.children.iter() {
            child.print_tree();
        }

    }
}


fn main() {
    let data: String = fs::read_to_string("src/input.txt").unwrap();
    let mut root = TreeNode::new("dupa", 3);

    let mut c1 = TreeNode::new("odbyt1", 2);
    let mut c2 = TreeNode::new("odbyt2", 2);

    let mut c3 = TreeNode::new("hej", 1);

    c1.parent = Some(Box::new(root.clone()));
    c2.parent = Some(Box::new(root.clone()));
    c3.parent = Some(Box::new(c1.clone()));
    
    c1.add_child(c3);
    root.add_child(c1);
    root.add_child(c2);

    root.print_tree();
    // println!("{}", data);
}
