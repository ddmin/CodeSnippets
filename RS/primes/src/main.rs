use std::ops::{FnOnce, RangeInclusive};
use std::thread;
use std::thread::JoinHandle;
use std::time::Instant;

const LIMIT: usize = 100000;
const MAX_THREADS: usize = 4;

#[derive(Debug)]
enum Divisibility {
    Prime(usize),
    Composite(usize),
}

impl Divisibility {
    fn from(n: usize) -> Divisibility {
        match is_prime(n) {
            true => Divisibility::Prime(n),
            false => Divisibility::Composite(n),
        }
    }
}

fn time<F: FnOnce(usize) -> Vec<Divisibility>>(f: F, arg: usize) {
    let now = Instant::now();
    let result = f(arg);
    let time = now.elapsed().as_millis();
    println!("Time: {}ms", time);
}

fn is_prime(n: usize) -> bool {
    let upper_limit = (n as f64).sqrt() as i64 + 1;

    for i in 2..upper_limit {
        if n % (i as usize) == 0 {
            return false;
        }
    }
    true
}

fn divvy_task(n: usize, workers: usize) -> Vec<RangeInclusive<usize>> {
    let mut current = 2;
    let increment = (n - 2) / workers;
    let mut leftovers = (n - 2) % workers;

    let mut work_list = Vec::new();
    for _ in 0..workers - 1 {
        if leftovers > 0 {
            work_list.push(current..=current + increment + 1);
            current += increment + 2;
            leftovers -= 1;
        } else {
            work_list.push(current..=current + increment);
            current += increment + 1;
        }
    }

    work_list.push(current..=n);
    work_list
}

fn single_threaded(n: usize) -> Vec<Divisibility> {
    (2..=n).map(|n| Divisibility::from(n)).collect()
}

fn multi_threaded(n: usize) -> Vec<Divisibility> {
    let mut threads = Vec::new();
    let work_list = divvy_task(n, MAX_THREADS);

    for range in work_list {
        threads.push(thread::spawn(move || {
            range.map(|n| Divisibility::from(n)).collect()
        }));
    }

    threads
        .into_iter()
        .map(|thread: JoinHandle<Vec<Divisibility>>| thread.join().unwrap())
        .flatten()
        .collect::<Vec<Divisibility>>()
}

fn main() {
    println!("Multi Threaded");
    time(multi_threaded, LIMIT);

    println!();

    println!("Single Threaded");
    time(single_threaded, LIMIT);
}
