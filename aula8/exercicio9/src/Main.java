import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        Map<Integer, List<Map.Entry<Integer, Double>>> adj = new HashMap<>();
        Map<Integer, Ponto> ponto = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int andar = scanner.nextInt();
            double x = scanner.nextDouble();
            double y = scanner.nextDouble();
            ponto.put(i, new Ponto(andar, x, y));
            adj.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int pontoA = scanner.nextInt();
            int pontoB = scanner.nextInt();
            String tipo = scanner.next();
            double costAB = 0.0;
            double costBA = 0.0;

            if (tipo.equals("walking") || tipo.equals("stairs")) {
                costAB = distanciaEucli(ponto.get(pontoA), ponto.get(pontoB));
                costBA = costAB;
            } else if (tipo.equals("lift")) {
                costAB = 1.0;
                costBA = 1.0;
            } else if (tipo.equals("escalator")) {
                costAB = 1.0;
                costBA = 3.0 * distanciaEucli(ponto.get(pontoA), ponto.get(pontoB));
            }

            adj.get(pontoA).add(new AbstractMap.SimpleEntry<>(pontoB, costAB));
            adj.get(pontoB).add(new AbstractMap.SimpleEntry<>(pontoA, costBA));
        }

        int q = scanner.nextInt();
        double[][] distancias = new double[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(distancias[i], Double.MAX_VALUE);
            distancias[i][i] = 0.0;
        }

        for (int i = 0; i < n; i++) {
            for (Map.Entry<Integer, Double> vizinho : adj.get(i)) {
                distancias[i][vizinho.getKey()] = vizinho.getValue();
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (distancias[i][k] + distancias[k][j] < distancias[i][j]) {
                        distancias[i][j] = distancias[i][k] + distancias[k][j];
                    }
                }
            }
        }

        for (int i = 0; i < q; i++) {
            int origem = scanner.nextInt();
            int destino = scanner.nextInt();
            List<Integer> caminho = menor(adj, origem, destino);
            StringBuilder saida = new StringBuilder();

            for (int j = 0; j < caminho.size(); j++) {
                saida.append(caminho.get(j));
                if (j < caminho.size() - 1) {
                    saida.append(" ");
                }
            }

            System.out.println(saida.toString());
        }
    }

    private static double distanciaEucli(Ponto p1, Ponto p2) {
        return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2) + Math.pow(p1.andar*5 - p2.andar*5, 2));
    }

    private static List<Integer> menor(Map<Integer, List<Map.Entry<Integer, Double>>> adj, int origem, int destino) {
        int n = adj.size();
        double[] distancias = new double[n];
        int[] pred = new int[n];
        Arrays.fill(distancias, Double.MAX_VALUE);
        distancias[origem] = 0.0;
        pred[origem] = -1;

        PriorityQueue<Map.Entry<Integer, Double>> priorityQueue = new PriorityQueue<>(Comparator.comparingDouble(Map.Entry::getValue));
        priorityQueue.add(new AbstractMap.SimpleEntry<>(origem, 0.0));

        while (!priorityQueue.isEmpty()) {
            Map.Entry<Integer, Double> atual = priorityQueue.poll();
            int pontoAtual = atual.getKey();
            double distanciaAtual = atual.getValue();

            if (distanciaAtual > distancias[pontoAtual]) {
                continue;
            }

            for (Map.Entry<Integer, Double> vizinho : adj.get(pontoAtual)) {
                int pontoVizinho = vizinho.getKey();
                double distVizinho = distanciaAtual + vizinho.getValue();

                if (distVizinho < distancias[pontoVizinho]) {
                    distancias[pontoVizinho] = distVizinho;
                    pred[pontoVizinho] = pontoAtual;
                    priorityQueue.add(new AbstractMap.SimpleEntry<>(pontoVizinho, distVizinho));
                }
            }
        }

        List<Integer> path = new ArrayList<>();
        int curr = destino;
        while (curr != -1) {
            path.add(curr);
            curr = pred[curr];
        }

        Collections.reverse(path);
        return path;
    }

    static class Ponto {
        int andar;
        double x;
        double y;

        Ponto(int andar, double x, double y) {
            this.andar = andar;
            this.x = x;
            this.y = y;
        }
    }
}
