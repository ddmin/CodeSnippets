use std::fmt;

/// An implementation of the `List` data structure in Rust.
///
/// # Examples
/// ```
/// use fundamentals::lists::List;
///
/// let mut list = List::new();
/// list.push(1);
/// list.push(2);
///
/// assert_eq!(list.size(), 2);
/// assert_eq!(list.get(0), Some(1));
///
/// assert_eq!(list.pop(), Some(2));
/// assert_eq!(list.size(), 1);
///
/// list.set(0, 7);
/// assert_eq!(list.get(0), Some(7));
/// ```
pub struct List<T>
where
    T: Copy + Default + fmt::Display + fmt::Debug,
{
    elements: Vec<T>,
    size: usize,
    capacity: usize,
}

#[macro_export]
macro_rules! list {
    ( $( $x:expr ),* ) => {
        {
            let mut _temp_list = List::new();
            $(
                _temp_list.push($x);
            )*
            _temp_list
        }
    };
}

impl<T> List<T>
where
    T: Copy + Default + fmt::Display + fmt::Debug,
{
    /// Constructs a new, empty List<T>.
    /// # Examples
    /// ```
    /// use fundamentals::lists::List;
    /// let mut list: List<i32> = List::new();
    /// ```
    pub fn new() -> List<T> {
        List {
            elements: vec![<T as Default>::default()],
            size: 0,
            capacity: 1,
        }
    }

    /// Return the number of elements inside the list.
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let list = list![1, 2, 3];
    /// assert_eq!(list.size(), 3);
    /// ```
    pub fn size(&self) -> usize {
        self.size
    }

    /// Return an `Option` of the element located at the index,
    /// and return `None` if out of bounds.
    ///
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let list = list![1, 2, 3, 4, 5];
    /// assert_eq!(Some(2), list.get(1));
    /// assert_eq!(Some(4), list.get(3));
    /// assert_eq!(None, list.get(5));
    /// ```
    pub fn get(&self, index: usize) -> Option<T> {
        if index >= self.size {
            return None;
        }
        Some(self.elements[index])
    }

    /// Set the element at `index` to `element`.
    /// # Panics
    /// Panics if the `index` is out of bounds.
    ///
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let mut list = list![1, 2, 3, 4, 5];
    /// list.set(1, 6);
    /// assert_eq!(Some(6), list.get(1));
    /// ```
    pub fn set(&mut self, index: usize, element: T) {
        assert!(
            index < self.size,
            "error: index {} out of bounds (size: {})",
            index,
            self.size
        );
        self.elements[index] = element;
    }

    // Double the capacity of the list
    fn double_capacity(&mut self) -> Vec<T> {
        self.capacity *= 2;
        vec![<T as Default>::default(); self.capacity]
    }

    /// Appends an element to the back of the list.
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let mut list = list![1, 2];
    /// list.push(3);
    /// assert_eq!(list.to_string(), "List [1, 2, 3]");
    /// ```
    pub fn push(&mut self, element: T) {
        if self.size + 1 > self.capacity {
            let mut temp = self.double_capacity();
            for i in 0..self.size {
                temp[i] = self.elements[i];
            }
            temp[self.size] = element;
            self.elements = temp;
        } else {
            self.elements[self.size] = element;
        }
        self.size += 1;
    }

    /// Inserts an element at position `index` within the list,
    /// shifting all elements after it to the right.
    ///
    /// # Panics
    /// Panics if `index > size`
    ///
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let mut list = list![1, 2, 3];
    /// list.insert(1, 4);
    /// assert_eq!(list.to_string(), "List [1, 4, 2, 3]");
    /// list.insert(4, 5);
    /// assert_eq!(list.to_string(), "List [1, 4, 2, 3, 5]");
    /// ```
    pub fn insert(&mut self, index: usize, element: T) {
        assert!(
            index <= self.size,
            "error: index {} out of bounds (size: {})",
            index,
            self.size
        );
        if index == self.size {
            self.push(element);
            return;
        }
        if self.size + 1 > self.capacity {
            let mut temp = self.double_capacity();
            for i in (index..self.size).rev() {
                temp[i + 1] = self.elements[i];
            }
            temp[index] = element;
            for i in 0..index {
                temp[i] = self.elements[i];
            }

            self.elements = temp;
        } else {
            for i in (index..self.size).rev() {
                self.elements[i + 1] = self.elements[i];
            }
            self.elements[index] = element;
        }

        self.size += 1;
    }

    /// Removes the last element from a list and returns it,
    /// or `None` if it is empty.
    ///
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let mut list = list![1, 2, 3];
    /// assert_eq!(list.pop(), Some(3));
    /// assert_eq!(list.to_string(), "List [1, 2]");
    /// ```
    pub fn pop(&mut self) -> Option<T> {
        if self.size == 0 {
            return None;
        }
        self.size -= 1;
        Some(self.elements[self.size])
    }

    /// Removes and returns the element at position `index` within the list,
    /// shifting all elements after it to the left.
    ///
    /// # Panics
    /// Panics if `index` is out of bounds.
    ///
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let mut list = list![1, 2, 3];
    /// list.remove(1);
    /// assert_eq!(list.to_string(), "List [1, 3]");
    /// ```
    pub fn remove(&mut self, index: usize) {
        assert!(
            index < self.size,
            "error: index {} out of bounds (size: {})",
            index,
            self.size
        );
        for i in index..self.size - 1 {
            self.elements[i] = self.elements[i + 1];
        }
        self.size -= 1;
    }

    /// Reverses the order or elements in the slice, in place.
    ///
    /// # Examples
    /// ```
    /// use fundamentals::list;
    /// use fundamentals::lists::List;
    ///
    /// let mut list = list![1, 2, 3];
    /// list.reverse();
    /// assert_eq!(list.to_string(), "List [3, 2, 1]");
    /// ```
    pub fn reverse(&mut self) {
        let mut temp = vec![<T as Default>::default(); self.capacity];
        for i in 0..self.size {
            temp[i] = self.elements[(self.size - 1) - i];
        }
        self.elements = temp;
    }
}

impl<T> From<&[T]> for List<T>
where
    T: Copy + Default + fmt::Display + fmt::Debug,
{
    fn from(slice: &[T]) -> List<T> {
        let mut temp_list = List::new();
        for element in slice.to_owned() {
            temp_list.push(element);
        }
        temp_list
    }
}

impl<T> fmt::Display for List<T>
where
    T: Copy + Default + fmt::Display + fmt::Debug,
{
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "List [")?;
        for i in 0..self.size {
            if i != 0 {
                write!(f, ", ")?;
            }
            write!(f, "{}", self.elements[i])?;
        }
        write!(f, "]")
    }
}
