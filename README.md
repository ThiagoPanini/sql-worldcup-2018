# SQL World Cup Russia 2018
A  ideia se baseia no seguinte anseio: criar algo único e totalmente sem compromisso relacionado a Copa do Mundo Russia 2018, utilizando, a princípio, a linguagem <b>SQL</b> como base. A utilização
e o aprimoramento dos diversos conceitos aprendidos ao longo da caminhada acadêmica são as principais motivações deste projeto e, com a adição de algo extremamente apaixonante presente no dia-a-dia de grande parte da sociedade como a Copa do Mundo, o trabalho a apresentado a seguir possui encorajamento suficiente pra se tornar referência para projetos futuros dentro deste mesmo escopo.

<img src="https://www.bodog.net/wp-content/uploads/2018/01/statistics_copa_do_mundo-1.jpg"/>

# Primeiros Passos

Levado pelos recentes estudos, o projeto tem como primeiro alicerce a aplicação de conceitos de SQL para controlar, dentro um Banco de Dados, os fatos ocorridos durante a Copa do Mundo. Visando aitribuir uma forma dinâmica ao aprendizado, pretende-se criar e atualizar eventos relevantes dentro de um Sistema de Gerenciamento de Banco de Dados. 

# Softwares utilizados

<a href="https://www.lucidchart.com/users/login">Lucidchart</a> - Modelagem dos dados e criação de diagramas UML.

<a href="https://www.postgresql.org/download/">PostgreSQL</a> - SGBD utilizado para o gerenciamento das Queries.

<a href="https://www.pgadmin.org/download/">pgAdmin4</a> - Interface via browser para utilização do Postgres.

<a href="http://www.eclipse.org/downloads/">Eclipse</a> - Eclipse IDE for Java Developers(integrações JDBC e JPA com Hibernate).

<a href="https://drive.google.com/file/d/17hz1C3DqXLvEzx7oEXj6Pd3XVvYIIM_i/view?usp=sharing">postgresql-42.2.2.jar</a> - Driver JDBC para Eclipse/Postgres.

<a href="https://drive.google.com/file/d/1jAukrD8r_SIKNsKO5mwVGZGWqR9ej6b4/view?usp=sharing">libs_postgres</a> - Libs para utilização do Hibernate com Eclipse/Postgres.


# Modelagem de Dados 

Sabe-se que a linguagem SQL está sempre em pauta. Saber manipula-la é <i>essencial</i>. Unir a <b>modelagem</b> de um conceito presente no cotidiano de muitas pessoas foi a maneira encontrada para instigar um projeto dinâmico e de fácil entendimento por parte de contribuidores e espectadores. 

A modelagem dos dados é uma etapa crucial que deve preceder a implementação física do modelo em um SGBD. Para o projeto em questão, foram utilizadas as ferramentas disponíveis na plataforma <b>Lucidchart</b>. O modelo pode ser visualizado abaixo:
<p>
<a href="http://pt-br.tinypic.com?ref=syo2ol" target="_blank"><img src="http://i66.tinypic.com/syo2ol.jpg" border="0" alt="Image and video hosting by TinyPic"></a>
</p>
Foram obtidas diversas versões do modelo acima e, da mesma forma, outras diversas versões foram adaptadas e passadas por processos de normalização para otimização de tabelas e relações. Os atributos foram definidos de acordo com a utilidade do projeto e a possibilidade de captar dados reais referentes a tais campos através dos jogos propriamente ditos.
Contudo, a modelagem acima ainda não está isenta de alterações, dada a divulgação pública do projeto e sua abertura à opiniões externas, sejam estas oriundas de amigos próximos ou simplesmente de simpatizantes do assunto.

ALTERAÇÕES NA MODELAGEM:
- Inserido campo id_fase na tabela <b>Seleção</b> como sendo Chave Estrangeira da tabela <b>Fase</b>;

# PostgreSQL

Dessa forma, o próximo passo se deu no sentido de implementar as tabelas de acordo com o Diagrama acima apresentado. Foi instalado o Banco de Dados PostgreSQL no Linux Ubuntu 18.04, bem como a interface pgadmin4 para auxiliar nas consultas/solicitações.

<img src="https://pplware.sapo.pt/wp-content/uploads/2015/11/post_04.jpg"/>


# 1.Tabela Seleção
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### CREATE TABLE selecao
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

Para a criação da tabela responsável por referenciar as seleções presentes neste modelo de Copa do Mundo, foi utilizada a seguinte sintaxe:

```
CREATE TABLE selecao(
id_selecao serial PRIMARY KEY NOT NULL,
nome_selecao character varying(50),
continente character varying(50));
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### INSERT INTO selecao
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

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
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### SELECT * FROM selecao
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

<a href="http://pt-br.tinypic.com?ref=300zosp" target="_blank"><img src="http://i67.tinypic.com/300zosp.png" border="0" alt="Image and video hosting by TinyPic"></a>

_


# 2.Tabela Grupo_Selecoes
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### CREATE TABLE grupo_selecoes;
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

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

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### INSERT INTO grupo_selecoes;
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

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
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### SELECT * FROM grupo_selecoes
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

<a href="http://pt-br.tinypic.com?ref=34hc26f" target="_blank"><img src="http://i68.tinypic.com/34hc26f.png" border="0" alt="Image and video hosting by TinyPic"></a>

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### INNER JOIN selecao ON grupo_selecoes.id_selecao = selecao.id_selecao
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

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

# 3.Tabela Fase
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### CREATE TABLE fase
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
A criação desta tabela tem por objetivo organizar, durante as partidas, a respectiva fase que representa tal partida. Em outras palavras, com esse indexador será possível conhecer o "nível" de partida tratado.

```
CREATE TABLE fase
id_fase serial smallint PRIMARY KEY NOT NULL CHECK(id_fase <=5),
nome_fase varchar(50);
```

CONSTRAINTS:
- id_fase é Chave Primária, não pode ser nulo e também não pode ser maior que 5;
- nome_fase irá receber a descrição da fase por meio de palavra única.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### INSERT INTO fase 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

```
INSERT INTO fase (nome_fase) values
('Grupos'), ('Oitavas'), ('Quartas'), ('Semi'), ('Final');
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
### SELECT * FROM fase
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

<a href="http://pt-br.tinypic.com?ref=23jpobn" target="_blank"><img src="http://i65.tinypic.com/23jpobn.png" border="0" alt="Image and video hosting by TinyPic"></a>

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
<i>ADENDO: Necessidade de alteração na tabela <b>selecao</b></i>

Após a inclusão dos dados na tabela <b>fase</b>, houve a ideia de referenciar também o id_fase dentro da tabela selecao, proporcionando a visualização da fase atual de cada seleção dentro de sua própria tabela.

Dessa forma, a sintaxe para inserção de um novo campo na tabela selecao se deu por:

```
ALTER TABLE selecao ADD COLUMN id_fase smallint REFERENCES fase default 1;
```

A partir do comando acima, foi adicionado o atributo id_fase à todos os itens da tabela selecao, sendo seu resultado final dado por:

<a href="http://pt-br.tinypic.com?ref=n33p94" target="_blank"><img src="http://i68.tinypic.com/n33p94.png" border="0" alt="Image and video hosting by TinyPic"></a>
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# 4.Tabela Estádio
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
### CREATE TABLE estadio
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
A tabela estadio irá armazenar o nome e a capacidade de todos os estádios sede de jogos.

```
CREATE TABLE estadio(
id_estadio serial PRIMARY KEY,
nome_estadio varchar(50),
capacidade integer NOT NULL CHECK(capacidade > 0);
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
### INSERT INTO estadio
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Para finalizar a criação da tabela <b>estadio</b>, serão adicionados todos os estádios que irão sediar algum jogo da Copa.

```
INSERT INTO estadio (nome_estadio, capacidade, cidade_est) values
('Lujinik', 80000, 'Moscou'),
('Spartak', 45000, 'Moscou'),
('Estádio de São Petesburgo', 67000, 'São Petesburgo'),
...);
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
### SDLECT * FROM estadio
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Por fim, o resultado final apresentado pela tabela, após a inserção dos dados foi:

<a href="http://pt-br.tinypic.com?ref=f2sqxs" target="_blank"><img src="http://i65.tinypic.com/f2sqxs.png" border="0" alt="Image and video hosting by TinyPic"></a>




# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
