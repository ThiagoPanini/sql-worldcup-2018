# SQL World Cup Russia 2018
A  ideia se baseia no seguinte anseio: criar algo único e totalmente sem compromisso relacionado a Copa do Mundo Russia 2018, utilizando, a princípio, a linguagem <b>SQL</b> como base. A utilização
e o aprimoramento dos diversos conceitos aprendidos ao longo da caminhada acadêmica são as principais motivações deste projeto e, com a adição de algo extremamente apaixonante presente no dia-a-dia de grande parte da sociedade como a Copa do Mundo, o trabalho a apresentado a seguir possui encorajamento suficiente pra se tornar referência para projetos futuros dentro deste mesmo escopo.

<img src="https://www.bodog.net/wp-content/uploads/2018/01/statistics_copa_do_mundo-1.jpg"/>

# Primeiros Passos

Levado pelos recentes estudos, o projeto tem como primeiro alicerce a aplicação de conceitos de SQL para controlar, dentro um Banco de Dados, os fatos ocorridos durante a Copa do Mundo. Visando aitribuir uma forma dinâmica ao aprendizado, pretende-se criar e atualizar eventos relevantes dentro de um Sistema de Gerenciamento de Banco de Dados. 

# Softwares utilizados

- <a href="https://www.lucidchart.com/users/login">Lucidchart</a> - Modelagem dos dados e criação de diagramas UML.

- <a href="https://www.postgresql.org/download/">PostgreSQL</a> - SGBD utilizado para o gerenciamento das Queries.

- <a href="https://www.pgadmin.org/download/">pgAdmin4</a> - Interface via browser para utilização do Postgres.

- <a href="http://www.eclipse.org/downloads/">Eclipse</a> - Eclipse IDE for Java Developers(integrações JDBC e JPA com Hibernate).

- <a href="https://drive.google.com/file/d/17hz1C3DqXLvEzx7oEXj6Pd3XVvYIIM_i/view?usp=sharing">postgresql-42.2.2.jar</a> - Driver JDBC para Eclipse/Postgres.

- <a href="https://drive.google.com/file/d/1jAukrD8r_SIKNsKO5mwVGZGWqR9ej6b4/view?usp=sharing">libs_postgres</a> - Libs para utilização do Hibernate com Eclipse/Postgres.


# Modelagem de Dados 

Sabe-se que a linguagem SQL está sempre em pauta. Saber manipula-la é <i>essencial</i>. Unir a <b>modelagem</b> de um conceito presente no cotidiano de muitas pessoas foi a maneira encontrada para instigar um projeto dinâmico e de fácil entendimento por parte de contribuidores e espectadores. 

A modelagem dos dados é uma etapa crucial que deve preceder a implementação física do modelo em um SGBD. Para o projeto em questão, foram utilizadas as ferramentas disponíveis na plataforma <b>Lucidchart</b>. O modelo pode ser visualizado abaixo:

<a href="http://pt-br.tinypic.com?ref=syo2ol" target="_blank"><img src="http://i66.tinypic.com/syo2ol.jpg" border="0" alt="Image and video hosting by TinyPic"></a>

Foram obtidas diversas versões do modelo acima e, da mesma forma, outras diversas versões foram adaptadas e passadas por processos de normalização para otimização de tabelas e relações. Os atributos foram definidos de acordo com a utilidade do projeto e a possibilidade de captar dados reais referentes a tais campos através dos jogos propriamente ditos.

Contudo, a modelagem acima ainda não está isenta de alterações, dada a divulgação pública do projeto e sua abertura à opiniões externas, sejam estas oriundas de amigos próximos ou simplesmente de simpatizantes do assunto.


ALTERAÇÕES NA MODELAGEM:
- Inserido campo id_fase na tabela <b>Seleção</b> como sendo Chave Estrangeira da tabela <b>Fase</b>;

# PostgreSQL

Dessa forma, o próximo passo se deu no sentido de implementar as tabelas de acordo com o Diagrama acima apresentado. Foi instalado o Banco de Dados PostgreSQL no Linux Ubuntu 18.04, bem como a interface pgadmin4 para auxiliar nas consultas/solicitações.

<img src="https://pplware.sapo.pt/wp-content/uploads/2015/11/post_04.jpg"/>


# 1. Tabela Seleção


### CREATE TABLE selecao
---

Para a criação da tabela responsável por referenciar as seleções presentes neste modelo de Copa do Mundo, foi utilizada a seguinte sintaxe:

```
CREATE TABLE selecao(
id_selecao serial PRIMARY KEY NOT NULL,
nome_selecao character varying(50),
continente character varying(50));
```

---
### INSERT INTO selecao
---

Para a inserção das seleções dentro da tabela, foi utilizada uma sintaxe que permitiu inserir todos os dados de uma única vez, sem a repetição da query <i>INSERT INTO</i>.

```
INSERT INTO selecao (nome_selecao, continente) values
('Rússia', 'Europa'),
('Arábia Saudita', 'Ásia'),
('Egito', 'Ásia'),
('Uruguai', 'América do Sul'),
('Portugal', 'Europa'),
('Espanha', 'Europa'),
...);
```

---
### SELECT * FROM selecao
---

<a href="http://pt-br.tinypic.com?ref=300zosp" target="_blank"><img src="http://i67.tinypic.com/300zosp.png" border="0" alt="Image and video hosting by TinyPic"></a>

_


# 2. Tabela Grupo_Selecoes

---
### CREATE TABLE grupo_selecoes;
---

A tabela grupo_selecoes tem por finalidade referenciar cada seleção criada através de seu respectivo grupo e armazenar, em seus registros, a condição atual dentro do grupo (pontos, vitórias, derrotas, empates, etc...).

```
CREATE TABLE grupo_selecoes(
nome_grupo char NOT NULL,
id_selecao smallint NOT NULL references selecao,
pontos smallint NOT NULL CHECK (pontos >= 0) default 0,
jogos smallint NOT NULL CHECK (pontos >= 0) default 0,
vitorias smallint NOT NULL CHECK (pontos >= 0) default 0,
empates smallint NOT NULL CHECK (pontos >= 0) default 0,
derrotas smallint NOT NULL CHECK (pontos >= 0) default 0,
PRIMARY KEY (nome_grupo, id_selecao),
CHECK (nome_grupo in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')));
```

CONSTRAINTS: 
- Nenhum campo deve ser nulo;
- O campo id_selecao funciona como Chave Estrangeira da tabela selecao,
- Os campos nome_grupo e id_selecao, juntos, atuam como uma Chave Primária Composta,
- Os campos pontos, jogos, vitorias, empates e derrotas, não podem ser nulos, possuem valor default = 0 e, por fim, possuem restrição de negativos,
- O campo nome_grupo deve estar entre os caracteres listados.

---
### INSERT INTO grupo_selecoes;
---

A inserção dos valores se deu de modo único, ou seja, todos os valores foram colocados através de uma única Query. Um ponto a ser citado é o valor default dos demais atributos, tornando opcional sua declaração neste momento inicial.

```
INSERT INTO grupo_selecoes values
('A', 1),
('A', 2),
('A', 3),
('A', 4),
('B', 5),
('B', 6),
...
('H', 32);
```

---
### SELECT * FROM grupo_selecoes
---

<a href="http://pt-br.tinypic.com?ref=34hc26f" target="_blank"><img src="http://i68.tinypic.com/34hc26f.png" border="0" alt="Image and video hosting by TinyPic"></a>

---
### INNER JOIN selecao ON grupo_selecoes.id_selecao = selecao.id_selecao
---

O comando acima é responsável por mostrar, ao usuário, uma tabela de grupos com visualização mais fácil e dinâmica, snedo esta referenciada pelo <i>nome_selecao</i> e não pelo <i>id_selecao</i>, como ocorrido em SELECT * from grupo_selecoes. Para tal, é necessário utilizar a sintaxe INNER JOIN para realizar consultas em duas tabelas: <b>selecao</b> (contendo o nome da seleção em questão) e <b>grupo_selecoes</b> (contendo todos os demais atributos). Veja a sintaxe completa:

```
SELECT
grupo_selecoes.nome_grupo as grupo,
selecao.nome_selecao as selecao,
grupo_selecoes.pontos, grupo_selecoes.jogos, grupo_selecoes.vitorias, grupo_selecoes.empates, grupo_selecoes.derrotas
from grupo_selecoes
inner join selecao on grupo_selecoes.id_selecao = selecao.id_selecao
where grupo_selecoes.nome_grupo = 'E';
```

OBSERVAÇÕES:
- A sintaxe <b>AS</b> define um "apelido" ao nome da coluna;
- A sintaxe <i>tabela</i>.atributo é utilizada para separar os campos das tabelas envolvidas;
- As linhas 2, 3 e 4 do código acima especificam, na ordem, quais atributos serão mostrados na consulta;
- A sintaxe <b>FROM</b> especifica a tabela mais importante a ser consultada;
- O comando <b>INNER JOIN</b> especifica a tabela a ser "mesclada";
- O comando <b>ON</b> determina a condição na qual será realizada essa busca (FK - PK / id - id);
- A condição <b>WHERE</b> condiciona apenas a visualização de um grupo.

RESULTADO:

<a href="http://pt-br.tinypic.com?ref=2qn8mjn" target="_blank"><img src="http://i63.tinypic.com/2qn8mjn.png" border="0" alt="Image and video hosting by TinyPic"></a>

_

# 3. Tabela Fase

### CREATE TABLE fase
---
A criação desta tabela tem por objetivo organizar, durante as partidas, a respectiva fase que representa tal partida. Em outras palavras, com esse indexador será possível conhecer o "nível" de partida tratado.

```
CREATE TABLE fase
id_fase serial smallint PRIMARY KEY NOT NULL CHECK(id_fase <=5),
nome_fase varchar(50);
```

CONSTRAINTS:
- id_fase é Chave Primária, não pode ser nulo e também não pode ser maior que 5;
- nome_fase irá receber a descrição da fase por meio de palavra única.

---
### INSERT INTO fase 
---

```
INSERT INTO fase (nome_fase) values
('Grupos'), ('Oitavas'), ('Quartas'), ('Semi'), ('Final');
```
---
### SELECT * FROM fase
---

<a href="http://pt-br.tinypic.com?ref=23jpobn" target="_blank"><img src="http://i65.tinypic.com/23jpobn.png" border="0" alt="Image and video hosting by TinyPic"></a>

---
<i>ADENDO: Necessidade de alteração na tabela <b>selecao</b></i>

Após a inclusão dos dados na tabela <b>fase</b>, houve a ideia de referenciar também o id_fase dentro da tabela selecao, proporcionando a visualização da fase atual de cada seleção dentro de sua própria tabela.

Dessa forma, a sintaxe para inserção de um novo campo na tabela selecao se deu por:

```
ALTER TABLE selecao ADD COLUMN id_fase smallint REFERENCES fase default 1;
```

A partir do comando acima, foi adicionado o atributo id_fase à todos os itens da tabela selecao, sendo seu resultado final dado por:

<a href="http://pt-br.tinypic.com?ref=n33p94" target="_blank"><img src="http://i68.tinypic.com/n33p94.png" border="0" alt="Image and video hosting by TinyPic"></a>

_

# 4. Tabela Estádio


### CREATE TABLE estadio
--- 

A tabela estadio irá armazenar o nome e a capacidade de todos os estádios sede de jogos.

```
CREATE TABLE estadio(
id_estadio serial PRIMARY KEY,
nome_estadio varchar(50),
capacidade integer NOT NULL CHECK(capacidade > 0);
```
---
### INSERT INTO estadio
---
Para finalizar a criação da tabela <b>estadio</b>, serão adicionados todos os estádios que irão sediar algum jogo da Copa.

```
INSERT INTO estadio (nome_estadio, capacidade, cidade_est) values
('Lujinik', 80000, 'Moscou'),
('Spartak', 45000, 'Moscou'),
('Estádio de São Petesburgo', 67000, 'São Petesburgo'),
...);
```

---
### SELECT * FROM estadio
---

Por fim, o resultado final apresentado pela tabela, após a inserção dos dados foi:

<a href="http://pt-br.tinypic.com?ref=f2sqxs" target="_blank"><img src="http://i65.tinypic.com/f2sqxs.png" border="0" alt="Image and video hosting by TinyPic"></a>

_

# 5. Tabela Árbitro

### CREATE TABLE arbitro
---
A tabela em questão irá armazenar o nome, a nacionalidade e a quantidade de partidas referentes aos árbitros selecionados para a Copa do Mundo Rússia 2018.

```
CREATE TABLE arbitro(
id_arbitro serial PRIMARY KEY,
nome_arbitro varchar(50),
nacionalidade varchar(50) NOT NULL,
qtd_partidas smallint NOT NULL default 0);
```

---
### INSERT INTO arbitro
---
Após a criação da tabela, foram reunidos os dados de todos os árbitros participantes da Copa e, através da Query de inserção, tais dados foram inseridos na tabela de acordo com a sintaxe abaixo:

```
INSERT INTO arbitro (nome_arbitro, nacionalidade) values
(‘Enrique Cáceres’, ‘Paraguai’),
(‘Andrés Cunha’, ‘Uruguai’),
(‘Néstor Pitana’, ‘Argentina’),
(‘Sandro Meira Ricci’, ‘Brasil’),
(‘Wilmar Roldán’, ‘Colômbia’),
(‘Felix Brych’, ‘Alemanha’),
(‘Cüneyt Çakır’, ‘Turquia’),
(...);
```

---
### SELECT * FROM arbitro
---

Dessa forma, a seleção dos valores da tabela arbitro tem como resultado:

<a href="http://pt-br.tinypic.com?ref=5xudch" target="_blank"><img src="http://i63.tinypic.com/5xudch.png" border="0" alt="Image and video hosting by TinyPic"></a>

_

# 6. Tabela Partida

### CREATE TABLE partida
---
Após toda a preparação necessária, é chegado o momento de criação das duas principais tabelas desta modelagem: <i>Partida</i> e <i>Selecao_partidas</i>, onde ambas serão responsáveis pela organização dos jogos entre as seleções, bem como os atributos e variantes que ocorrem a cada partida, como Gols, Cartões, uso do VAR, etc. Dessa forma, a criação da tabela <i>Partida</i> se deu por:

```
CREATE TABLE partida(
id_partida serial PRIMARY KEY,
id_fase smallint REFERENCES fase,
data_partida timestamp NOT NULL,
id_estadio smallint REFERENCES estadio,
publico integer CHECK(publico > 0),
id_arbitro smalint REFERENCES arbitro,
uso_var boolean DEFAULT false);
```

---
### INSERT INTO partida
---

A inserção de dados dentro da tabela <b>partida</b> se deu através de pesquisas em sites esportivos a fim de reunir informações específicas de cada partida, como o estádio, o público, o árbitro e até mesmo o uso ou não da tecnologia do VAR. Em muitos momentos, houve dificuldades em encontrar esta informação, uma vez que os principais sites esportivos não reuniam todas elas em um único lugar, ou muitas vezes não as mostravam. De toda forma, a sintaxe para inserção destes dados foi a seguinte:


```
INSERT INTO partida (id_fase, data_partida, id_estadio, publico, id_arbitro, uso_var)
values (1, '14-06-2018 12:00:00', 1, 78011, 24, false);
```
O codigo acima exemplifica a inserçao da partida de abertura da Copa do Mundo. 

---
### SELECT * FROM partida
---

Abaixo e apresentada a tabela partida apos a query de seleçao:

<a href="http://pt-br.tinypic.com?ref=sg3k7s" target="_blank"><img src="http://i64.tinypic.com/sg3k7s.png" border="0" alt="Image and video hosting by TinyPic"></a>

Entretanto, visando dinamizar a apresentação dos dados ao usuário, foi utilizada uma sintaxe de seleção diferenciada contemplando conceitos de <b>INNER JOIN</b> com as tabelas <b>arbitro</b> e <b>estadio</b>:

```
SELECT partida.id_partida, fase.nome_fase, partida.data_partida, partida.id_estadio, estadio.nome_estadio,
partida.publico, partida.id_arbitro, arbitro.nome_arbitro, arbitro.qtd_partidas, partida.uso_var
FROM partida
INNER JOIN fase ON partida.id_fase = fase.id_fase
INNER JOIN arbitro ON partida.id_arbitro = arbitro.id_arbitro
INNER JOIN estadio ON partida.id_estadio = estadio.id_arbitro
ORDER BY partida.id_partida;
```

Dessa forma, foi possível visualizar, a cada inserção da tabela partida, seus respectivos dados de estadio e arbitro. 

Um outro a ponto a ser considerado foi o incremento, dentro da tabela arbitro, do atributo qtd_partidas de acordo com a seleção do id do arbitro em cada partida:

```
UPDATE arbitro SET qtd_partidas = qtd_partidas + 1 WHERE id_arbitro = x;
```
Onde 'x' é, de fato, o id do árbitro referente a partida que está sendo cadastrada.
