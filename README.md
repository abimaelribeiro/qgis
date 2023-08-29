# Map theme maker in Pyqgis <a href="readme.md"><img src="/assets/eua.png"></a>

Este script permite que usuários do qgis agilize a produção de mapas usando a funcionalidade themas do Qgis, usando Pyqgis.

### Que problema o script resolve?

Este script foi elaborado para otimizar a produção de mapas no QGIS, quando se tem a necessidade de produzir muitos temas.

Geralmente a criação mapas no Qgis é feito manualmente e o usuário precisa criar temas manualmente por meio do Gerenciador de temas.

Para isso o usuário precisa selecionar as camadas que serão utilizadas em cada mapa e salvar os temas um a um. 

A criação de temas, por sua vez, torna-se trabalhosa se o projeto tiver muitos temas. Por exemplo: Se o projeto tiver 1000 mapas, serão 1000 temas relacionados e "N" camadas para cada tema configurados manualmente.

### Como eu faço para utilizar o script?

Para otimizar essa tarefa execute o passo a passo abaixo:

1 - Abra e organize o seu projeto no Qgis;

2 - Ative as camadas fixas que serão exibidas em todos os mapas;

3 - Escolha as camadas que comporão a base de cada tema e insira o nome deles na lista da  denominada layerList.

```csharp
layerList = ["layer1", "layer2", "layer3"];
```

4 - Abra um terminal Python no Qgis e execute o script;

### Observações:

Se você tiver camadas ativas o script montará um novo tema para cada camada da lista com as camadas que estão ativas. Desligue a visibilidade das camadas se você não quiser elas apareçam.

## Tecnologias utilizadas

- [PyQGIS](https://docs.qgis.org/3.28/en/docs/pyqgis_developer_cookbook/index.html){:target="_blank" rel="noopener"};
