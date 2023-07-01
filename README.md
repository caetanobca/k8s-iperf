# Kubernetes iperf 

Nesse repositorio contem os scripts responsaveis para avaliar a performance da rede de um cluster Kubernetes, usando o iperf. O funcionamento desse teste se da a partir do deploy de um server iperf em um dos nós e um client em cada um dos worker nodes, para assim realizar o teste de rede entre pods que estão no mesmo nó ou em nós diferentes.

## Como usar 

### Realizando os testes 

Escolha o nó que você deseja que hospede o server e então rode o seguinte comando

```bash
./k8s-iperf [NODE_NAME] > results.txt
```

Você deve realizar esse teste para cada um dos worker nodes.

### Motando os CSVs

Uma vez realizados os testes. Vamos montar os CSVs que serão ultilizados para gerar os box plots.

Devem ser criados dois CSVs, um com as informações de pods em nós diferentes e outro sobre pods no mesmo nó, ambos os arquivos devem  seguir esse formato:

| interval | transfer_GB | bandwidth_Gb_s |
|---|---|---|
| duração do teste | GB transferidos | Largura de manda em Gb/s |

### Plotando os Box Plots

Para instalar as dependencias use o seguinte comando

```pip3
pip3 install -r python_scripts/requirements.txt
```

Para criar os Box Plots, basta executar o seguinte comando:

```python3
python3 python_scripts/plot.py [CAMINHO_PARA_CSV_NÓS_DIFERENTES] [CAMINHO_PARA_CSV_MESMO_NÓ]
```

## Melhorias

* Criar script que automatiza todo o processo
* Criar o CSV automaticamente a partir das saidas do script inicial