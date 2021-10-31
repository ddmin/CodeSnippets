use std::cmp::Ordering;
use std::collections::HashMap;
use std::sync::Arc;
use std::sync::Mutex;
use std::thread;

type PrimeTable = Arc<Mutex<HashMap<usize, bool>>>;

pub struct Worker {
    n: usize,
    hash_table: PrimeTable,
}

impl Worker {
    fn new(n: usize, hash_table: PrimeTable) -> Worker {
        Worker { n, hash_table }
    }

    fn check_prime(&self) {
        let mut hash_table = self.hash_table.lock().unwrap();
        println!("Worker {} checking prime", self.n);
        if is_prime(self.n) {
            hash_table.insert(self.n, true);
            println!("Worker {} found prime!", self.n);
        } else {
            hash_table.insert(self.n, false);
        }
    }
}

fn multi_threaded(n: usize) {
    let primes = HashMap::<usize, bool>::new();
    let primes = Arc::new(Mutex::new(primes));
    let threads = Vec::<thread::JoinHandle<()>>::new();

    for i in 2..n {
        let worker = Worker::new(i, Arc::clone(&primes));
        thread::spawn(move || worker.check_prime());
    }

    for thread in threads {
        thread.join().unwrap();
    }

    let mut primes = primes.lock().unwrap();
    let mut primes: Vec<(usize, bool)> = primes.drain().collect();
    primes.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

    for (a, b) in primes.iter() {
        println!("{}: {}", a, b);
    }
}

fn single_threaded(n: usize) {
    for i in 2..n {
        println!("{}: {}", i, is_prime(i));
    }
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

fn main() {
    let n = 500_000;
    single_threaded(n);
    // multi_threaded(n);
}
