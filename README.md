<h1 align="center">Harmonógrafos</h1>

# Descrição do Projeto
Plotagem animada de um pêndulo amortecido 1D e a trajetória de um pêndulo caótico(harmonógrafo) 2D e 3D.

--- 
## Teoria
Um harmonógrafo é um aparelho mecânico que emprega vários pêndulos acoplados para criar imagens geométricas. Os desenhos criados normalmente são curvas de Lissajous, ou até mesmo desenhos de maior complexidade. As imagens são complexas, mas bonitas e elegantes.

Essas imagens podem ser criadas anexando um objeto que escreva como canena ou lápis na parte inferior do pêndulo. Assim, à medida que o pêndulo se move, esses padrões são desenhados. Até mesmo um simples harmonógrafo como descrito pode criar [elipses](https://pt.wikipedia.org/wiki/Elipse), [espirais](https://pt.wikipedia.org/wiki/Espiral), [figura oito](https://en.wiktionary.org/wiki/figure_eight) e outras [figuras de Lissajous](https://pt.wikipedia.org/wiki/Curvas_de_Lissajous).

### Harmonógrafo em um eixo - Pêndulo Amortecido
Um harmonógrafo cria suas figuras usando os movimentos de pêndulos amortecidos. O movimento de um pêndulo amortecido ao longo da eixo qualquer (eixo ![x](https://latex.codecogs.com/gif.latex?x) por exemplo) é descrito pela equação:

![Pêndulo](https://latex.codecogs.com/gif.latex?x%28t%29%20%3D%20Asin%282%5Cpi%20ft%20&plus;%20p%29e%5E%7B%28-dt%29%7D)

### Harmonógrafos em dois eixos
Se esse pêndulo puder se mover em torno de dois eixos (em forma circular ou elíptica), devido ao princípio de superposição, o movimento de uma haste conectada ao fundo do pêndulo ao longo de um eixo será descrito pela equação:

![Eixo x](https://latex.codecogs.com/gif.latex?x%28t%29%20%3D%20A_1sen%282%5Cpi%20f_1t%20&plus;%20p_1%29e%5E%7B%28-d_1t%29%7D%20&plus;%20A_2sen%282%5Cpi%20f_2t%20&plus;%20p_2%29e%5E%7B%28-d_2t%29%7D)

Se dois pêndulos estão se movendo ao longo de dois eixos, as equações gerais de movimento do pêndulo são dadas por:

![Eixo X](https://latex.codecogs.com/gif.latex?x%28t%29%20%3D%20A_1sen%282%5Cpi%20f_1t%20&plus;%20p_1%29e%5E%7B%28-d_1t%29%7D%20&plus;%20A_2sen%282%5Cpi%20f_2t%20&plus;%20p_2%29e%5E%7B%28-d_2t%29%7D)

![Eixo y](https://latex.codecogs.com/gif.latex?y%28t%29%20%3D%20A_3sen%282%5Cpi%20f_3t%20&plus;%20p_3%29e%5E%7B%28-d_3t%29%7D%20&plus;%20A_4sen%282%5Cpi%20f_4t%20&plus;%20p_4%29e%5E%7B%28-d_4t%29%7D)

Dessa forma, temos 16 parâmetros e cada combinação distinta desses parâmetros produzirá uma figura diferente, logo teremos infinitas possibilidades.

---
## Animações

### Pêndulo Amortecido
![Pendulo_Amortecido](https://user-images.githubusercontent.com/65929471/97743346-46487d00-1ac4-11eb-972b-e8e1affa4a18.gif)

### Harmonógrafo 2D
![2D](https://user-images.githubusercontent.com/65929471/97744853-b0fab800-1ac6-11eb-8f61-669373d98a75.gif)


### Harmonógrafo 3D
![Harmo3D](https://user-images.githubusercontent.com/65929471/97738270-e4d0e000-1abc-11eb-8abb-0a45eed71ce5.gif)

---
### Referências:

[Harmonograph 1](https://en.wikipedia.org/wiki/Harmonograph)

[Harmonograph 2](http://paulbourke.net/geometry/harmonograph/) ![aa](https://user-images.githubusercontent.com/65929471/89193696-c1a99980-d57c-11ea-86d3-9ae0796bf046.gif)
