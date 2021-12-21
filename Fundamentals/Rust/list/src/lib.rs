pub mod lists;

#[cfg(test)]
mod list_tests {
    use super::*;
    use lists::List;

    #[test]
    fn test_list_macro() {
        let list = list![1, 2, 3];
        assert_eq!(list.to_string(), "List [1, 2, 3]");
        let empty: List<i32> = list![];
        assert_eq!(empty.to_string(), "List []");
        let char_list: List<char> = list!['a'];
        assert_eq!(char_list.to_string(), "List [a]");
        let str_slice_list: List<&str> = list!["a", "b", "c"];
        assert_eq!(str_slice_list.to_string(), "List [a, b, c]");
    }

    #[test]
    fn test_create_push_pop() {
        let mut list: List<i32> = List::new();
        assert_eq!(list.to_string(), "List []".to_string());

        // push
        list.push(1);
        assert_eq!(list.to_string(), "List [1]".to_string());
        list.push(2);
        assert_eq!(list.to_string(), "List [1, 2]".to_string());
        list.push(3);
        assert_eq!(list.to_string(), "List [1, 2, 3]".to_string());
        list.push(4);
        assert_eq!(list.to_string(), "List [1, 2, 3, 4]".to_string());
        list.push(5);
        assert_eq!(list.to_string(), "List [1, 2, 3, 4, 5]".to_string());

        // pop
        let item = list.pop();
        assert_eq!(item, Some(5));
        assert_eq!(list.to_string(), "List [1, 2, 3, 4]".to_string());

        let item = list.pop();
        assert_eq!(item, Some(4));
        assert_eq!(list.to_string(), "List [1, 2, 3]".to_string());

        let item = list.pop();
        assert_eq!(item, Some(3));
        assert_eq!(list.to_string(), "List [1, 2]".to_string());

        let item = list.pop();
        assert_eq!(item, Some(2));
        assert_eq!(list.to_string(), "List [1]".to_string());

        let item = list.pop();
        assert_eq!(item, Some(1));
        assert_eq!(list.to_string(), "List []".to_string());

        let item = list.pop();
        assert_eq!(item, None);
        assert_eq!(list.to_string(), "List []".to_string());
    }

    #[test]
    fn test_insert_and_remove() {
        let mut list: List<char> = List::new();
        assert_eq!(list.to_string(), "List []".to_string());

        // insert
        list.insert(0, 'a');
        assert_eq!(list.to_string(), "List [a]".to_string());
        list.insert(0, 'b');
        assert_eq!(list.to_string(), "List [b, a]".to_string());
        list.insert(1, 'c');
        assert_eq!(list.to_string(), "List [b, c, a]".to_string());
        list.insert(2, 'd');
        assert_eq!(list.to_string(), "List [b, c, d, a]".to_string());
        list.insert(2, 'e');
        assert_eq!(list.to_string(), "List [b, c, e, d, a]".to_string());
        list.insert(5, 'f');
        assert_eq!(list.to_string(), "List [b, c, e, d, a, f]".to_string());
        list.insert(5, 'g');
        assert_eq!(list.to_string(), "List [b, c, e, d, a, g, f]".to_string());
        list.insert(0, 'h');
        assert_eq!(
            list.to_string(),
            "List [h, b, c, e, d, a, g, f]".to_string()
        );

        // remove
        list.remove(2);
        assert_eq!(list.to_string(), "List [h, b, e, d, a, g, f]".to_string());
        list.remove(6);
        assert_eq!(list.to_string(), "List [h, b, e, d, a, g]".to_string());
        list.remove(1);
        assert_eq!(list.to_string(), "List [h, e, d, a, g]".to_string());
        list.remove(0);
        assert_eq!(list.to_string(), "List [e, d, a, g]".to_string());
        list.remove(2);
        assert_eq!(list.to_string(), "List [e, d, g]".to_string());
        list.remove(2);
        assert_eq!(list.to_string(), "List [e, d]".to_string());
        list.remove(1);
        assert_eq!(list.to_string(), "List [e]".to_string());
        list.remove(0);
        assert_eq!(list.to_string(), "List []".to_string());
    }

    #[test]
    fn test_get_and_set() {
        let mut list: List<f32> = List::new();

        for i in 0..4 {
            list.push(1.0 + 0.1 * (i as f32));
        }

        // get
        assert_eq!(list.get(0), Some(1.0));
        assert_eq!(list.get(1), Some(1.1));
        assert_eq!(list.get(2), Some(1.2));
        assert_eq!(list.get(3), Some(1.3));

        // set
        for i in 0..list.size() {
            list.set(i, list.get(i).unwrap() * 2f32);
        }

        // get
        assert_eq!(list.get(0), Some(2.0));
        assert_eq!(list.get(1), Some(2.2));
        assert_eq!(list.get(2), Some(2.4));
        assert_eq!(list.get(3), Some(2.6));
    }

    #[test]
    fn test_reverse() {
        let mut list = List::new();
        for i in 0..6 {
            list.push(i);
        }

        assert_eq!(list.to_string(), "List [0, 1, 2, 3, 4, 5]");
        list.reverse();
        assert_eq!(list.to_string(), "List [5, 4, 3, 2, 1, 0]");

        // empty list
        let mut list: List<char> = List::new();
        list.reverse();
        assert_eq!(list.to_string(), "List []");

        // single item
        list.push('a');
        list.reverse();
        assert_eq!(list.to_string(), "List [a]");
    }
}
