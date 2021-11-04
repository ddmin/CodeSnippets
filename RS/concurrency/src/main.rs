use std::thread;

struct ThreadPool {
    threads: Vec<Worker>,
}

impl ThreadPool {
    fn new(n: usize) -> ThreadPool {
        assert!(n > 0);
        let threads = Vec::with_capacity(n);
        ThreadPool { threads }
    }

    fn execute(&self) {
        let worker = thread::spawn(|| {});
    }
}

struct Worker {
    id: usize,
}

impl Worker {
    fn new(id: usize) -> Worker {
        Worker { id }
    }

    fn execute(&self) {
        println!("Worker {}", self.id);
    }
}

fn main() {
    let pool = ThreadPool::new(10);
    for _ in 0..100 {
        pool.execute();
    }
}
