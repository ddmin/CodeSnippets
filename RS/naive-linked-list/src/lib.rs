pub mod linked;

#[cfg(test)]
mod list_tests {
    use super::*;

    use linked::LinkedList;

    #[test]
    fn test_linked_list_init() {
        let mut linked_list: LinkedList<i32> = LinkedList::new();
        assert_eq!(linked_list.to_string(), "LinkedList []");
        linked_list.prepend(3);
        assert_eq!(linked_list.to_string(), "LinkedList [3]");
        linked_list.prepend(6);
        assert_eq!(linked_list.to_string(), "LinkedList [6, 3]");
        linked_list.prepend(9);
        assert_eq!(linked_list.to_string(), "LinkedList [9, 6, 3]");
        linked_list.prepend(12);
        assert_eq!(linked_list.to_string(), "LinkedList [12, 9, 6, 3]");
        linked_list.prepend(1000);
        assert_eq!(linked_list.to_string(), "LinkedList [1000, 12, 9, 6, 3]");
    }

    #[test]
    fn test_linked_list_append() {
        let mut linked_list: LinkedList<&str> = LinkedList::new();
        assert_eq!(linked_list.to_string(), "LinkedList []");
        linked_list.push("apple");
        assert_eq!(linked_list.to_string(), "LinkedList [apple]");
        linked_list.push("banana");
        assert_eq!(linked_list.to_string(), "LinkedList [apple, banana]");
        linked_list.push("Cantaloupe");
        assert_eq!(
            linked_list.to_string(),
            "LinkedList [apple, banana, Cantaloupe]"
        );
        linked_list.push("DURIAN");
        assert_eq!(
            linked_list.to_string(),
            "LinkedList [apple, banana, Cantaloupe, DURIAN]"
        );
        linked_list.push("");
        assert_eq!(
            linked_list.to_string(),
            "LinkedList [apple, banana, Cantaloupe, DURIAN, ]"
        );
        linked_list.push("fig");
        assert_eq!(
            linked_list.to_string(),
            "LinkedList [apple, banana, Cantaloupe, DURIAN, , fig]"
        );
    }

    #[test]
    fn test_linked_list_set_and_get() {
        let mut l = LinkedList::<char>::new();
        for c in 'a'..'d' {
            l.push(c);
        }
        assert_eq!(l.to_string(), "LinkedList [a, b, c]");
        assert_eq!(l.size(), 3);

        l.set(0, 'd');
        assert_eq!(l.to_string(), "LinkedList [d, b, c]");
        assert_eq!(l.get(0), Some('d'));

        l.set(1, 'e');
        assert_eq!(l.to_string(), "LinkedList [d, e, c]");
        assert_eq!(l.get(1), Some('e'));

        l.set(2, 'f');
        assert_eq!(l.to_string(), "LinkedList [d, e, f]");
        assert_eq!(l.get(2), Some('f'));

        // set as push
        assert_eq!(l.size(), 3);
        l.set(3, 'g');
        assert_eq!(l.to_string(), "LinkedList [d, e, f, g]");
        assert_eq!(l.get(3), Some('g'));
        assert_eq!(l.size(), 4);

        assert_eq!(l.size(), 4);
        l.set(4, 'h');
        assert_eq!(l.to_string(), "LinkedList [d, e, f, g, h]");
        assert_eq!(l.get(4), Some('h'));
        assert_eq!(l.size(), 5);

        // query element out of bound yields None
        assert_eq!(l.get(5), None);
        assert_eq!(l.get(100), None);
    }

    #[test]
    fn test_linked_list_macro() {
        let mut l = linked![1.0, 1.1, 1.2, 1.3, 1.4, 1.5];
        let items = vec![1.0, 1.1, 1.2, 1.3, 1.4, 1.5];

        assert_eq!(l.to_string(), "LinkedList [1, 1.1, 1.2, 1.3, 1.4, 1.5]");

        for i in items.iter().rev() {
            let cons = l.pop();
            assert_eq!(cons, Some(*i));
        }

        for _ in 0..100 {
            let cons = l.pop();
            assert_eq!(cons, None);
        }
    }
}
