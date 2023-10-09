# Detecação de Intrusos/Malwares

Aqui estão alguns artigos que selecionei de um survey do IEEE Access chamado: [IoT Malware Analysis Using Federated Learning](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10012334)

### [73] - [Federated learning for mawlare detection in IoT devices (Elsevier)](https://www.sciencedirect.com/science/article/pii/S1389128621005582)
 
Um framework que usa Federated Learning para detectar malwares que podem afetar dispositivos IoT.

Uma estratégia utilizada é monitorar as atividades de um dispositivo corromptido e coletar fingerprints de comportamento ou perfil. Exemplos, são a comunicação de rede, uso de recursos do dispositvo infectado etc. Com isso é possível utilizar técnicas de ML/DL para detecar se um dispositivo está infectado com malwares. Entretanto por questões de privacidade é interessante utilizar o Federated Learning que atingi acurácia semelhante ao modelo centralizado.

Acurácia: 98.5%

### [77] - [FIDChain: Federated Intrusion Detection System for Blockchain-Enabled IoT Healthcare Applications (MDPI)](https://www.mdpi.com/2227-9032/10/6/1110)

Proposta de um uma rede neural artificial para detecção de intrusos em aplicações IoT de saúde. Foi utilizado blockchain.

### [78] - [FELIDS: Federated learning-based intrusion detection system for agricultural Internet of Things (Elsevier)](https://www-sciencedirect.ez19.periodicos.capes.gov.br/science/article/pii/S0743731522000570)

Combinaram FL + SDN + blockchain para a detecção de ataques a dispositivos IoT da agricultura 4.0.

O método proposto possui taxa de detecção igual ou mais alta do que os métodos centralizados.

### [86] - [Federated IoT attack detection using decentralized edge data (Elsevier)](https://www.researchgate.net/publication/358185549_Federated_IoT_security_attack_detection_using_decentralized_edge_data)

Uso de um deep autoencoder para detectar ataques de botnets usando dados de trafégo decentralizados dos dispositivos.

Acurácia: 98%

### [87] - [Internet Traffic classification with Federated Learning (MDPI)](https://www.mdpi.com/2079-9292/10/1/27)

É proposto um protocolo de classificação de tráfego de Federated Learning, o qual consegue atingir uma acurácia comparável aos modelos centralizados tradicionais de deep learning para IoT sem sofrer problemas de vazamento de dados.

Resolve um problema de tolerância a falhas na comunicação entre o cliente e o servidor e opera em um cenário em que a aplicação para classificar pode ser dinamicamente alocada.

Acurácia: 92%

# Mais artigos de outro survey

Aqui estão os artigos do survey geral de IoT com aprendizado federado: [Federated Learning for Internet of Things: A comprehensive Survey (IEEE)](https://ieeexplore-ieee-org.ez19.periodicos.capes.gov.br/stamp/stamp.jsp?tp=&arnumber=9415623)


### [82] - [DÏoT: A Federated Self-learning Anomaly Detection System for IoT (2019)](https://browse.arxiv.org/pdf/1804.07474.pdf)

Alega ser o primeiro artigo a usar FL para detecção de intrusos/anomalias.

### [83] - [Collaborative Learning Model for Cyberatack Detection Systems in IoT Industry 4.0 (IEEE)](https://ieeexplore-ieee-org.ez19.periodicos.capes.gov.br/stamp/stamp.jsp?tp=&arnumber=9120761)

Desenvolvimento de "filtros" inteligentes os quais podem ser implantados em IoT gateways a fim de detectar e prevenir ciberataques.

### [84] - [Federated Wireless Network Intrusion Detection (IEEE)](https://ieeexplore-ieee-org.ez19.periodicos.capes.gov.br/stamp/stamp.jsp?tp=&arnumber=9005507)

Uso de FL para detecção de intrusos em redes sem fio. Foi feita apenas uma simulação

### [86] - [Less is More: A privacy-respecting Android malware classifier using Federated Learning](https://browse.arxiv.org/pdf/2007.08319.pdf)

Um framework classificador que utiliza Aprendizado Federado para detecção e classificação de aplicativos android maliciosos enquanto respeita a privacidade dos dados do usuário.

### [104] - [Multi-Task Network Anomaly Detection using Federated Learning (ACM)](https://dl-acm-org.ez19.periodicos.capes.gov.br/doi/pdf/10.1145/3368926.3369705)

Detectar e analizar o tráfego de rede usando aprendizado federado.
