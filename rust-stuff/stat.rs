use std::collections::HashMap;

fn main() {
    let vec: Vec<f32> = vec![1.0, 1.0, 1.0, 2.0, 2.0, 5.0, 10.0];

    let mut sum: f32 = 0.0;
    for i in &vec {
        sum += i;
    }

    let mut counter = HashMap::new();
    for i in &vec {
        let n = *i as i32;
        let c = counter.entry(n).or_insert(0);
        *c += 1;
    }

    let mut mode = 0;
    let mut most_frequent = 0;

    for (k, v) in &counter {
        if most_frequent < *v {
            mode = *k;
            most_frequent = *v;
        }
    }

    let length: f32 = vec.len() as f32;
    let mean = sum / length;
    let median = vec[vec.len() / 2];

    println!("List: {:?}", vec);
    println!("Mean: {}", mean);
    println!("Median: {}", median);
    println!("Mode: {}", mode);
}
