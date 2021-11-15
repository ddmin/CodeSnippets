use std::boxed::Box;
use std::fmt;

#[derive(Clone, Debug)]
pub enum LinkedList<T>
where
    T: Copy + Default + fmt::Display + fmt::Debug,
{
    Cons {
        element: T,
        next: Box<LinkedList<T>>,
        size: usize,
    },
    None,
}

#[derive(Debug)]
enum RecursiveOp {
    Increment(usize),
    Decrement(usize),
    None,
}

#[allow(unused_variables)]
impl<T> LinkedList<T>
where
    T: Copy + Default + fmt::Display + fmt::Debug,
{
    pub fn new() -> LinkedList<T> {
        LinkedList::None
    }

    pub fn size(&self) -> usize {
        match self {
            LinkedList::Cons { size, .. } => *size,
            LinkedList::None => 0,
        }
    }

    pub fn prepend(&mut self, element: T) {
        *self = LinkedList::Cons {
            element,
            next: Box::new(self.clone()),
            size: match self {
                LinkedList::Cons { size, .. } => *size + 1,
                LinkedList::None => 1,
            },
        };
    }

    pub fn push(&mut self, element: T) {
        let last = self.get_last_mut(RecursiveOp::Increment(1));
        *last = LinkedList::Cons {
            element,
            next: Box::new(LinkedList::None),
            size: 1,
        };
    }

    pub fn set(&mut self, index: usize, element: T) {
        let cons;
        match self {
            LinkedList::Cons { size, .. } => {
                assert!(
                    *size >= index,
                    "error: index {} out of bounds (size: {})",
                    index,
                    *size
                );

                // If the index you are setting is equal to the size of the list
                // you instead push the item onto the list.
                // Pushing the item on the list requires that you increase the size
                // of the list, thus you increment each previous list item.
                cons = if *size == index {
                    self.get_position_mut(index, RecursiveOp::Increment(1))
                } else {
                    self.get_position_mut(index, RecursiveOp::None)
                }
            }
            LinkedList::None => {
                assert!(index == 0, "error: index {} out of bounds (size: 0)", index,);
                cons = self.get_position_mut(index, RecursiveOp::None);
            }
        };

        match cons {
            LinkedList::Cons { element: e, .. } => *e = element,
            LinkedList::None => cons.push(element),
        }
    }

    pub fn pop(&mut self) -> Option<T> {
        match self.size() {
            0 => return None,
            1 => {
                let element = self.get(0);
                *self = LinkedList::None;
                return element;
            }
            _ => (),
        };

        let new_last = self.get_position_mut(self.size() - 1, RecursiveOp::Decrement(1));
        match new_last {
            LinkedList::Cons { element, next, .. } => {
                *next = Box::new(LinkedList::None);
                Some(*element)
            }
            LinkedList::None => None,
        }
    }

    // TODO: insert implementation for linked list
    pub fn insert(&mut self, index: usize, element: T) {
        todo!()
    }

    // TODO: remove implementation for linked list
    pub fn remove(&mut self, index: usize) {
        todo!()
    }

    // TODO: reverse implementation for linked list
    pub fn reverse(&mut self) {
        todo!()
    }

    pub fn get(&self, index: usize) -> Option<T> {
        let cons = self.get_position(index);
        match cons {
            LinkedList::Cons { element, .. } => return Some(*element),
            LinkedList::None => return None,
        }
    }

    fn get_position(&self, position: usize) -> &LinkedList<T> {
        if position == 0 {
            return self;
        }

        match self {
            LinkedList::Cons { next, .. } => next.get_position(position - 1),
            LinkedList::None => self,
        }
    }

    fn get_position_mut(&mut self, position: usize, op: RecursiveOp) -> &mut LinkedList<T> {
        if position == 0 {
            return self;
        }

        match self {
            LinkedList::Cons { size, next, .. } => {
                match op {
                    RecursiveOp::Increment(i) => *size += i,
                    RecursiveOp::Decrement(i) => *size -= i,
                    RecursiveOp::None => (),
                };
                next.get_position_mut(position - 1, op)
            }
            LinkedList::None => self,
        }
    }

    fn get_last_mut(&mut self, op: RecursiveOp) -> &mut LinkedList<T> {
        match self {
            LinkedList::Cons { size, next, .. } => {
                match op {
                    RecursiveOp::Increment(i) => *size += i,
                    RecursiveOp::Decrement(i) => *size -= i,
                    RecursiveOp::None => (),
                };
                next.get_last_mut(op)
            }
            LinkedList::None => self,
        }
    }

    fn string_recursive(&self, s: String) -> String {
        match self {
            LinkedList::Cons { element, next, .. } => {
                next.string_recursive(format!("{}, {}", s, element))
            }
            LinkedList::None => s,
        }
    }
}

impl<T> fmt::Display for LinkedList<T>
where
    T: Copy + Default + fmt::Display + fmt::Debug,
{
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "LinkedList [")?;

        let mut elements = String::new();
        if let LinkedList::Cons { element, next, .. } = self {
            elements = next.string_recursive(elements);
            write!(f, "{}{}", element, elements)?;
        }
        write!(f, "]")
    }
}

#[macro_export]
macro_rules! linked {
    ( $( $x:expr ),* ) => {
        {
            let mut _temp_list = LinkedList::new();
            $(
                _temp_list.push($x);
            )*
            _temp_list
        }
    };
}

