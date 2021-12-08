enum Loop {
    Within,
    Looped,
}

#[derive(Copy, Clone)]
struct LoopedInt {
    curr: i32,
    lower: i32,
    upper: i32,
}

impl LoopedInt {
    fn new(curr: i32, lower: i32, upper: i32) -> LoopedInt {
        LoopedInt { curr, lower, upper }
    }

    fn get(self) -> i32 {
        self.curr
    }

    fn next(&mut self) -> Loop {
        self.curr += 1;
        if self.curr > self.upper {
            self.curr = self.lower;
            return Loop::Looped;
        }
        Loop::Within
    }
}

struct Triplet {
    base: LoopedInt,
    height: i32,
    hyp: i32,
    max: i32,
}

impl Triplet {
    fn is_pythagorean(&self) -> bool {
        self.base.get().pow(2) + self.height.pow(2) == self.hyp.pow(2)
    }

    fn next(&mut self) {
        self.hyp -= 1;
        match self.base.next() {
            Loop::Looped => {
                self.height += 1;
                let hypoteneuse = self.max - (self.base.get() + self.height);
                self.hyp = hypoteneuse;
            }
            Loop::Within => (),
        };
    }

    fn multiply(&self) -> i32 {
        self.base.get() * self.height * self.hyp
    }
}

fn main() {
    const SUM: i32 = 1000;

    let mut triangle = Triplet {
        base: LoopedInt::new(1, 1, SUM - 2),
        height: 1,
        hyp: SUM - 2,
        max: SUM,
    };

    while !triangle.is_pythagorean() {
        triangle.next();
    }

    println!(
        "{} {} {}",
        triangle.base.get(),
        triangle.height,
        triangle.hyp,
    );

    println!("Product: {}", triangle.multiply());
}
