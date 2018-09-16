#include <stdio.h>
#include <limits.h>

/*
    Dijkstra's shortest path algorithm

    This implementation takes a weighted graph of N nodes
    (in adjacency matrix form) and with the source node,
    returns the least cost path to each node.
*/

// Number of nodes we're solving for
#define N 9

void dijkstra(int graph[N][N], int src) {
    int res[N]; // Stores our results 
    bool nodes[N]; // Representation of vertices

    // Prepare for traversal
    for (int i = 0; i< N; i++) {
        res[i] = INT_MAX, nodes[i] = false;
    }

    res[src] = 0;

    // Find shortest paths
    for (int i = 0; i < N - 1; i++) {
        // Find the least cost path
        int min_value = INT_MAX, min;
        for (int n = 0; n < N; n++) {
            if (!nodes[n] && res[n] <= min_value) min_value = res[n], min = n;
        }

        // Traverse to vertice
        nodes[min] = true;

        // Update weights
        for (int n = 0; n < N; n++) {
            if (!nodes[n] && graph[min][n] && res[min] != INT_MAX && res[min]+graph[min][n] < res[n])
                res[n] = res[min] + graph[min][n];
        }

    }

    for (int i = 0; i < N; i++) 
        printf("%d - %d\n", i, res[i]);

}

int main () {
    // Adjancency matrix representation
    int graph[N][N] = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                      {4, 0, 8, 0, 0, 0, 0, 11, 0},
                      {0, 8, 0, 7, 0, 4, 0, 0, 2},
                      {0, 0, 7, 0, 9, 14, 0, 0, 0},
                      {0, 0, 0, 9, 0, 10, 0, 0, 0},
                      {0, 0, 4, 14, 10, 0, 2, 0, 0},
                      {0, 0, 0, 0, 0, 2, 0, 1, 6},
                      {8, 11, 0, 0, 0, 0, 1, 0, 7},
                      {0, 0, 2, 0, 0, 0, 6, 7, 0}
                     };

    dijkstra(graph, 0);

    return 0;
}
