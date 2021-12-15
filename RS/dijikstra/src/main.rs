use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: usize,
    position: usize,
}

// create a min-heap instead of a max-heap
impl Ord for State {
    fn cmp(&self, other: &State) -> Ordering {
        other
            .cost
            .cmp(&self.cost)
            .then_with(|| self.position.cmp(&other.position))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct Edge {
    node: usize,
    cost: usize,
}

fn dijikstra(adj_list: &Vec<Vec<Edge>>, start: usize, goal: usize) -> Option<usize> {
    // shortest distance to position
    let mut shortest_dist = (0..adj_list.len()).map(|_| usize::MAX).collect::<Vec<_>>();

    let mut heap = BinaryHeap::new();

    shortest_dist[start] = 0;
    heap.push(State {
        cost: 0,
        position: start,
    });

    while let Some(State { cost, position }) = heap.pop() {
        // goal has been reached, return length of path
        if position == goal {
            return Some(cost);
        }

        // shorter path exists
        if cost > shortest_dist[position] {
            continue;
        }

        // iterate through all adjacent positions
        for edge in &adj_list[position] {
            let next = State {
                cost: cost + edge.cost,
                position: edge.node,
            };

            // found new shortest path to position?
            if next.cost < shortest_dist[next.position] {
                heap.push(next);
                shortest_dist[next.position] = next.cost;
            }
        }
    }

    None
}

fn main() {
    let graph = vec![
        // Node 0
        vec![Edge { node: 2, cost: 10 }, Edge { node: 1, cost: 1 }],
        // Node 1
        vec![Edge { node: 3, cost: 2 }],
        // Node 2
        vec![
            Edge { node: 1, cost: 1 },
            Edge { node: 3, cost: 3 },
            Edge { node: 4, cost: 1 },
        ],
        // Node 3
        vec![Edge { node: 0, cost: 7 }, Edge { node: 4, cost: 2 }],
        // Node 4
        vec![],
    ];

    assert_eq!(dijikstra(&graph, 0, 1), Some(1));
    assert_eq!(dijikstra(&graph, 0, 3), Some(3));
    assert_eq!(dijikstra(&graph, 3, 0), Some(7));
    assert_eq!(dijikstra(&graph, 0, 4), Some(5));
    assert_eq!(dijikstra(&graph, 4, 0), None);

    println!("Distance from 0 to 1: {:?}", dijikstra(&graph, 0, 1));
    println!("Distance from 0 to 3: {:?}", dijikstra(&graph, 0, 3));
    println!("Distance from 3 to 0: {:?}", dijikstra(&graph, 3, 0));
    println!("Distance from 0 to 4: {:?}", dijikstra(&graph, 0, 4));
    println!("Distance from 4 to 0: {:?}", dijikstra(&graph, 4, 0));
}
