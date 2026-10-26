• Álgebra Relacional 

<u>Referência: Prof. Fábio Silvestre</u> 









Linguagens Formais de Consulta ao Modelo Relacional 

Álgebra Relacional - Linguagem procedural. 

Cálculo Relacional  - Linguagem nãoprocedural ou linguagem declarativa. 

<u>Referência: Prof. Fábio Silvestre</u> 

## Álgebra Relacional 

Provê um fundamento formal para operações do modelo relacional. 

Utilizada como base para implementar e otimizar as consultas nos sistemas gerenciadores de banco de dados relacional (SGBDRs). 

<u>Referência: Prof. Fábio Silvestre</u> 

### Operadores da Álgebra Relacional 

- *Seleção, indicado por σ (a letra grega sigma minúscula) 

- *Projeção, indicado pela letra grega pi 



<!-- Start of picture text -->
6 _|Selesio /Restisio | coats (Relagdo)<br>| me |Projesto | genes (Relagio) |<br>| - | Diferenza de conjuntos _[Relagaol -Relagao2_|<br>x [produto caresiano __|Relagdo1 x Relagio2 _|<br>tsi |rungio | Retagdot | Relag 02_|<br>|p |Renomesgio | psome(Relagao) —_|<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> 

#### Classificações da Álgebra Relacional quanto sua Origem 

- **_Fundamentais_** - cinco operadores operadores são ditos primitivos ou fundamentais, ou seja, através deles qualquer expressão de consulta de dados é possível. São eles: _seleção_ , _projeção_ , _produto cartesiano_ , _união_ e _diferença_ . 

- **_Derivados_** - derivam dos operadores fundamentais. São definidos para facilitar a especificação de certos procedimentos. São eles: _intersecção_ , _junção_ (normal e natural) e _divisão_ . 

- **_Especiais_** - Operadores que não se enquadram nos itens anteriores. São eles: _renomeação_ e _alteração_ . 

<u>Referência: Prof. Fábio Silvestre</u> 

- Classificações da Álgebra Relacional quanto ao 

- Número de Relações 

• **_Unários_** - operam em uma única tabela. São eles: _seleção, projeção, renomeação e alteração_ . 

• **_Binários_** - operam em duas tabelas. São eles: _união, interseção, diferença, produto cartesiano, junção_ e _divisão_ . 

<u>Referência: Prof. Fábio Silvestre</u> 

- **_Especiais_** - operadores adicionais, definidos pela álgebra relacional para manipulação de dados. São eles: _seleção_ , _projeção_ , _junção_ , _divisão_ , _renomeação_ e _alteração_ . 

Classificações da Álgebra Relacional quanto à Área Matemática 

- **_Teoria dos conjuntos_** - operadores usuais da teoria de conjuntos da matemática. São eles: _união_ , _interseção_ , _diferença_ e _produto cartesiano_ . 

- **_Funções matemáticas de agregação_** - funções matemáticas de agregação para uma coleção de valores de dados. Entre as mais comuns estão a _SOMA_ , _MÉDIA_ , _MÁXIMO_ , _MÍNIMO_ e _CONTADOR_ . 

<u>Referência: Prof. Fábio Silvestre</u> 

# Modelo de Dados de Exemplo 

**CHAVE PRIMÁRIA** 

###### **CHAVE ESTRANGEIRA** 

###### **CARGO** 

|**Código**|**Nome**|**Valor**|
|---|---|---|
|C1|Aux. Vendas|350,00|
|C3|Vendedor|800,00|
|C7|Diretor|2500,00|
|C2|Vigia|400,00|
|C5|Gerente|1000,00|
|C4|Aux. Cobrança|250,00|



||**DEPARTAMENTO**|
|---|---|
|**Código**|**Ramal**<br>**Nome**|
|D1|2246<br>Assit. Técnica|
|D2|2589<br>Estoque|
|D3|2772<br>Administração|
|D4|1810<br>Segurança|
|D5|2599<br>Vendas|
|D6|2688<br>Cobrança|



|||**FUNCIONARIO**||||
|---|---|---|---|---|---|
|**Numero**<br>|**Nome**<br>|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|101<br>|Luís Sampaio<br>|10/08/2003|M|C3|D5|
|104<br>|Carlos Pereira<br>|02/03/2004|M|C4|D6|
|134<br>|Jose Alves<br>|23/05/2002|M|C5|D1|
|121<br>|Luís Paulo Souza<br>|10/12/2001|M|C3|D5|
|195<br>|Marta Silveira<br>|05/01/2002|F|C1|D5|
|139<br>|Ana Luiza Magalhães<br>|12/01/2003|F|C4|D6|
|123<br>|Pedro Sergio Doto<br>|29/06/2003|M|C7|D3|
|148<br>|Larissa Silva<br>|01/06/2002|F|C4|D6|
|115<br>|Roberto Fernandes<br>|15/10/2003|M|C3|D5|
|of. Fábio Silvestre<br>22<br>|Sergio Nogueira<br>|10/02/2000|M|C2|D4|



<u>Referência: Prof. Fábio Silvestre</u> 

# Operação de Projeção 

**Conjunto de Entrada** 

- Nome_Coluna1, Nome_Coluna2, ..., Nome_ColunaN (Nome_Tabela) 

**Argumentos da Operação** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Operação de Projeção 

###### **Conjunto de Entrada** 

- Nome (FUNCIONARIO) 

###### **Argumentos da Operação** 

<u>Referência: Prof. Fábio Silvestre</u> | ~~an~~ 

# Representação Gráfica 

# da Operação de Projeção 

###### **FUNCIONARIO** 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|195|Marta Silveira|05/01/2002|F|C1|D5|
|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148|Larissa Silva|01/06/2002|F|C4|D6|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|22|Sergio Nogueira|10/02/2000|M|C2|D4|



**¶** Nome (FUNCIONARIO) 

|**Nome**|
|---|
|Luís Sampaio|
|Carlos Pereira|
|Jose Alves|
|Luís Paulo Souza|
|Marta Silveira|
|Ana Luiza Magalhães|
|Pedro Sergio Doto|
|Larissa Silva|
|Roberto Fernandes|
|Sergio Nogueira|



<u>Referência: Prof. Fábio Silvestre</u> 

Exemplo de Operação de Projeção 

###### **Conjunto de Entrada** 

¶  Nome, Sexo (FUNCIONARIO) LJ 

###### **Argumentos da Operação** 

<u>Referência: Prof. Fábio Silvestre</u> |<sup>~~ae~~</sup> 

# Representação Gráfica 

# da Operação de Projeção 

###### **FUNCIONARIO** 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|195|Marta Silveira|05/01/2002|F|C1|D5|
|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148|Larissa Silva|01/06/2002|F|C4|D6|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|22|Sergio Nogueira|10/02/2000|M|C2|D4|



**¶** Nome, Sexo (FUNCIONARIO) 

|**Nome**|**Sexo**|
|---|---|
|Luís Sampaio|M|
|Carlos Pereira|M|
|Jose Alves|M|
|Luís Paulo Souza|M|
|Marta Silveira|F|
|Ana Luiza Magalhães|F|
|Pedro Sergio Doto|M|
|Larissa Silva|F|
|Roberto Fernandes|M|
|Sergio Nogueira|M|



<u>Referência: Prof. Fábio Silvestre</u> 

# Operação de Seleção 

**Conjunto de Entrada** 

Predicado (Nome_Tabela) 

**Predicado da Operação** 

<u>Referência: Prof. Fábio Silvestre</u> J ~~s ae~~ 

<u>Referência: Prof. Fábio Silvestre</u> 

Exemplo de Operação de Seleção 

**Conjunto de Entrada** 

###### Sexo='M' (FUNCIONARIO) 

**Predicado da Operação** 

<u>Referência: Prof. Fábio Silvestre</u> | ~~an~~ 

### Representação Gráfica da Operação de Seleção 

###### **FUNCIONARIO** 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|195|Marta Silveira|05/01/2002|F|C1|D5|
|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148|Larissa Silva|01/06/2002|F|C4|D6|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|22|Sergio Nogueira|10/02/2000|M|C2|D4|



Sexo = 'M' (FUNCIONARIO) 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|rof. Fábio Silvestre<br>22|Sergio Nogueira|10/02/2000|M|C2|D4|



Exemplo de Operação de Seleção Utilizando _AND_ AND Operador 

**Conjunto de Entrada** oF Sexo = 'M' **^** Cod_Cargo = 'C3' (FUNCIONARIO) a) 

###### **Predicado da Operação** 

<u>Referência: Prof. Fábio Silvestre</u> ~~ae~~ 

### Representação Gráfica da Operação de Seleção com _AND_ 

###### **FUNCIONARIO** 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|195|Marta Silveira|05/01/2002|F|C1|D5|
|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148|Larissa Silva|01/06/2002|F|C4|D6|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|22|Sergio Nogueira|10/02/2000|M|C2|D4|



Sexo = 'M' **^** Cod_Cargo = 'C3' (FUNCIONARIO) 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|a: Prof. Fábio Silvestre<br>115|<br>Roberto Fernandes|15/10/2003|M|C3|D5|



Exemplo de Operação de Seleção Utilizando _OR_ OR Operador 

**Conjunto de Entrada** 

Sexo = 'M'    Cod_Cargo = 'C4' (FUNCIONARIO) Lo 

**Predicado da Operação** 

<u>Referência: Prof. Fábio Silvestre</u> ~~ae~~ 

|||Repres<br>|entaç<br>|ão<br>|Gráfi<br>|ca<br>|
|---|---|---|---|---|---|---|
|da O<br><br>|<br><br>|peração<br><br><br>|de S<br>**FUNCIONARI**<br><br>|eleç<br>**O**<br>|ão c|om<br>_OR_<br>OR|
|**Numero**<br><br><br>||**Nome**<br><br>a<br><br><br>|**Data_Admissao**<br><br>|**Sexo**<br>|**Cod_Cargo**|**Cod_Depto**|
|101<br><br><br>||Luís Sampaio<br><br>a<br><br><br>|10/08/2003<br><br>|M<br>|C3|D5|
|104<br><br><br>||Carlos Pereira<br><br>a<br><br><br>|02/03/2004<br><br>|M<br>|C4|D6|
|134<br><br><br>||Jose Alves<br><br>a<br>|23/05/2002<br>|M<br>|C5|D1|
|121<br>a<br>||Luís Paulo Souza<br>|10/12/2001<br>|M<br>|C3|D5|
|195<br><br>a <br>|<br>|Marta Silveira<br>a<br>|05/01/2002<br>|F<br>|C1|D5|
|139<br><br>||Ana Luiza Magalhães<br><br>a<br>|12/01/2003<br><br>|F<br>|C4|D6|
|123<br><br><br>||Pedro Sergio Doto<br><br><br><br>|29/06/2003<br><br>|M<br>|C7|D3|
|148<br><br><br>||Larissa Silva<br><br>a<br><br><br>|01/06/2002<br><br>|F<br>|C4|D6|
|115<br><br>||Roberto Fernandes<br><br>a<br>|15/10/2003<br><br>|M<br>|C3|D5|
|22<br>||Sergio Nogueira<br>|10/02/2000<br>|M<br>|C2|D4|
|||Sexo = 'M'<br>**q**<br>**^**<br><br>|Cod_Cargo = 'C4' (FUN<br><br><br>wy<br>|CIONARIO)<br><br>|||
|**Numero**<br>a <br>||**Nome**<br><br>|**Data_Admissao**<br><br>|**Sexo**<br><br>|**Cod_Cargo**<br>|**Cod_Depto**<br>|
|101<br>—_<br><br>||Luís Sampaio<br>~~—~~<br><br>|10/08/2003<br><br><br>|M<br><br><br>|C3<br><br>|D5<br><br>|
|104<br> <br><br>a||Carlos Pereira<br><br><br>|02/03/2004<br><br><br>|M<br><br><br>|C4<br><br>|D6<br><br>|
|134<br>||Jose Alves<br>|23/05/2002<br>|M<br>|C5|D1|
|121||Luís Paulo Souza|10/12/2001|M|C3|D5|
|139<br><br>||Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123<br><br>a||Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148<br><br><br><br>||Larissa Silva|01/06/2002|F|C4|D6|
|<br>115<br><br>||Roberto Fernandes|15/10/2003|M|C3|D5|
|rência: Prof. Fábio Silvestre<br>~~22~~<br><br>||Sergio Nogueira|10/02/2000|M|C2|D4|



~~=—~~ 

|o Si<br>~~-~~|
|---|



<u>Referência: Prof. Fábio Silvestre</u> 

Exemplo de Operação de Projeção com Seleção **Conjunto de Entrada** an ¶ Nome, Data_Admissao (    Sexo = 'M' (FUNCIONARIO)) LJ **Projeção Seleção** 

<u>Referência: Prof. Fábio Silvestre</u> |<sup>~~ae~~</sup> 

### Representação Gráfica 

### de Projeção com Seleção 

###### **FUNCIONARIO** 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|195|Marta Silveira|05/01/2002|F|C1|D5|
|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148|Larissa Silva|01/06/2002|F|C4|D6|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|22|Sergio Nogueira|10/02/2000|M|C2|D4|



###### ¶ Nome, Data_Admissao (    Sexo = 'M' (FUNCIONARIO)) 

|**Nome**|**Data_Admissao**|
|---|---|
|Luís Sampaio|10/08/2003|
|Carlos Pereira|02/03/2004|
|Jose Alves|23/05/2002|
|Luís Paulo Souza|10/12/2001|
|Pedro Sergio Doto|29/06/2003|
|Roberto Fernandes|15/10/2003|
|Sergio Nogueira|10/02/2000|



<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação de Projeção com Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 



<!-- Start of picture text -->
RESULTADO DA<br>PROJEÇÃO  ¶ Nome, Data_Admissao<br>RESULTADO DA<br>SELEÇÃO<br>   Sexo = 'M' (FUNCIONARIO)<br>TABELA<br>FUNCIONARIO<br>q<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação de Projeção com Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 



<!-- Start of picture text -->
RESULTADO DA<br>PROJEÇÃO  ¶ Nome, Data_Admissao<br>RESULTADO DA<br>SELEÇÃO<br>   Sexo = 'M' (FUNCIONARIO)<br>TABELA<br>FUNCIONARIO<br>q<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação de Projeção com Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 



<!-- Start of picture text -->
RESULTADO DA<br>PROJEÇÃO  ¶ Nome, Data_Admissao<br>RESULTADO DA<br>SELEÇÃO<br>   Sexo = 'M' (FUNCIONARIO)<br>TABELA<br>FUNCIONARIO<br>q<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação de Projeção com Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 



<!-- Start of picture text -->
RESULTADO DA<br>PROJEÇÃO  ¶ Nome, Data_Admissao<br>RESULTADO DA<br>SELEÇÃO<br>   Sexo = 'M' (FUNCIONARIO)<br>TABELA<br>FUNCIONARIO<br>q<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> 

Exemplo de Operação de Projeção com Seleção 

**Conjunto de Entrada** 

¶ Nome, Data_Admissao (    Sexo = 'M' ^ Cod_Cargo = 'C3' (FUNCIONARIO)) **Projeção Seleção** 

**Seleção** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Representação Gráfica de Projeção com Seleção 

###### **FUNCIONARIO** 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|195|Marta Silveira|05/01/2002|F|C1|D5|
|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148|Larissa Silva|01/06/2002|F|C4|D6|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|22|Sergio Nogueira|10/02/2000|M|C2|D4|



¶ Nome, Data_Admissao (    Sexo = 'M' **^** Cod_Cargo = 'C3' (FUNCIONARIO)) 

|**Nome**|**Data_Admissao**|
|---|---|
|Luís Sampaio|10/08/2003|
|Luís Paulo Souza|10/12/2001|
|Roberto Fernandes|15/10/2003|



<u>Referência: Prof. Fábio Silvestre</u> 

Exemplo de Operação de Projeção com Seleção 

**Conjunto de Entrada** 

¶ Nome, Data_Admissao (    Sexo = 'M'     Cod_Cargo = 'C4' (FUNCIONARIO)) **Projeção Seleção** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Representação Gráfica 

# de Projeção com Seleção 

###### **FUNCIONARIO** 

|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|---|---|---|---|---|---|
|101|Luís Sampaio|10/08/2003|M|C3|D5|
|104|Carlos Pereira|02/03/2004|M|C4|D6|
|134|Jose Alves|23/05/2002|M|C5|D1|
|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|195|Marta Silveira|05/01/2002|F|C1|D5|
|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
|123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
|148|Larissa Silva|01/06/2002|F|C4|D6|
|115|Roberto Fernandes|15/10/2003|M|C3|D5|
|22|Sergio Nogueira|10/02/2000|M|C2|D4|



¶ Nome, Data_Admissao (    Sexo = 'M'     Cod_Cargo = 'C4' (FUNCIONARIO)) 

|**Nome**|**Data_Admissao**|
|---|---|
|Luís Sampaio|10/08/2003|
|Carlos Pereira|02/03/2004|
|Jose Alves|23/05/2002|
|Luís Paulo Souza|10/12/2001|
|Ana Luiza Magalhães|12/01/2003|
|Pedro Sergio Doto|29/06/2003|
|Larissa Silva|01/06/2002|
|Roberto Fernandes|15/10/2003|
|Sergio Nogueira|10/02/2000|



<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação de Projeção com Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 

RESULTADO DA PROJEÇÃO ¶ Nome, Data_Admissao 

RESULTADO DA SELEÇÃO Sexo = 'M'    Cod_Cargo = 'C4' (FUNCIONARIO) 

TABELA FUNCIONARIO 

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação de Projeção com Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 

RESULTADO DA PROJEÇÃO ¶ Nome, Data_Admissao 

RESULTADO DA SELEÇÃO Sexo = 'M'    Cod_Cargo = 'C4' (FUNCIONARIO) 

TABELA FUNCIONARIO 

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação de Projeção com Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 

RESULTADO DA PROJEÇÃO ¶ Nome, Data_Admissao 

RESULTADO DA SELEÇÃO Sexo = 'M'    Cod_Cargo = 'C4' (FUNCIONARIO) 

TABELA FUNCIONARIO 

<u>Referência: Prof. Fábio Silvestre</u> 

# Produto Cartesiano 

**Tabela A** x **Tabela B** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Produto Cartesiano 

##### **Grupo_A** x **Grupo_B** 

###### **Grupo_A** 



<!-- Start of picture text -->
Grupo_A Grupo_B<br>Time Clube<br>Bahia Atlético-MG<br>São Paulo Cruzeiro<br>Palmeiras Grêmio<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> 

# Produto Cartesiano entre os Grupos 

**Grupo_A** x **Grupo_B** 



<!-- Start of picture text -->
Bahia Atlético-MG<br>São Paulo Cruzeiro<br>Palmeiras Grêmio<br>Grupo A Grupo B<br>O resultado do produto cartesiano de duas<br>relações é uma terceira relação contendo todas<br>as combinações possíveis entre os elementos das<br>Referência: Prof. Fábio Silvestre<br>relações originais.<br><!-- End of picture text -->

# Representação Gráfica do Produto Cartesiano 



<!-- Start of picture text -->
Grupo_A Grupo_B<br>Time Clube<br>Bahia Atlético-MG<br>São Paulo Cruzeiro<br>Palmeiras Grêmio<br><!-- End of picture text -->





###### **Grupo_A X Grupo_B** 



|**Time**|**Clube**|
|---|---|
|Bahia|Atlético-MG|
|Bahia|Cruzeiro|
|Bahia|Grêmio|
|São Paulo|Atlético-MG|
|São Paulo|Cruzeiro|
|São Paulo|Grêmio|
|Palmeiras|Atlético-MG|
|Palmeiras|Cruzeiro|
|Palmeiras|Grêmio|



<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Produto Cartesiano com Projeção e Seleção 

**Produto Cartesiano** 

¶ Funcionario.Nome, Funcionario.Data_Admissão  (     Cargo.Codigo = 'C4'  ^  Funcionario.Cod_Cargo = Cargo.Codigo ( FUNCIONARIO X CARGO)) 

**Projeção** 

**Seleção** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Representação Gráfica do Produto <u>Cartesiano com Projeção e Seleção</u> 

**CHAVE PRIMÁRIA** 

###### **CHAVE ESTRANGEIRA** 

||**CARGO**||||**FUNCIONARIO**||||
|---|---|---|---|---|---|---|---|---|
|**Código**|**Nome**|**Valor**|**Numero**|**Nome**|**Data_Admissao**|**Sexo**|**Cod_Cargo**|**Cod_Depto**|
|C1<br>Au|x. Vendas|350,00|101|Luís Sampaio|10/08/2003|M|C3|D5|
|C3<br>|Vendedor|800,00|104|Carlos Pereira|02/03/2004|M|C4|D6|
|C7|Diretor|2500,00|134|Jose Alves|23/05/2002|M|C5|D1|
|C2|Vigia|400,00|121|Luís Paulo Souza|10/12/2001|M|C3|D5|
|C5|Gerente|1000,00|195|Marta Silveira|05/01/2002|F|C1|D5|
|C4<br>Au|x. Cobrança|250,00|139|Ana Luiza Magalhães|12/01/2003|F|C4|D6|
||||123|Pedro Sergio Doto|29/06/2003|M|C7|D3|
||||148|Larissa Silva|01/06/2002|F|C4|D6|
||||115|Roberto Fernandes|15/10/2003|M|C3|D5|
||||22|Sergio Nogueira|10/02/2000|M|C2|D4|





###### **¶ Funcionario.Nome, Funcionario.Data_Admissão(     Cargo.Codigo = 'C4'  ^  Funcionario.Cod_Cargo = Cargo.Codigo ( FUNCIONARIO X CARGO))** 



|**Nome**|**Data_Admissao**|
|---|---|
|Carlos Pereira|02/03/2004|
|Ana Luiza Magalhães|12/01/2003|
|Larissa Silva|01/06/2002|



<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução do Produto Cartesiano com Projeção e Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 

RESULTADO DA PROJEÇÃO **¶** Funcionario.Nome, Funcionario.Data_Admissão 

RESULTADO DA SELEÇÃO Cargo.Codigo = 'C4' **^** Funcionario.Cod_Cargo = Cargo.Codigo 

RESULTADO DO PRODUTO CARTESIANO 

FUNCIONARIO x CARGO TABELA TABELA CARGO FUNCIONARIO 

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução do Produto Cartesiano com Projeção e Seleção 

Conjunto de dados processados ou 

que serão processados 

Conjunto de dados em processamento ou finalizado 

RESULTADO DA PROJEÇÃO **¶** Funcionario.Nome, Funcionario.Data_Admissão 

RESULTADO DA SELEÇÃO Cargo.Codigo = 'C4' **^** Funcionario.Cod_Cargo = Cargo.Codigo 

RESULTADO DO PRODUTO CARTESIANO 

FUNCIONARIO x CARGO 

TABELA TABELA CARGO FUNCIONARIO 

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução do Produto Cartesiano com Projeção e Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 

RESULTADO DA PROJEÇÃO **¶** Funcionario.Nome, Funcionario.Data_Admissão 

RESULTADO DA SELEÇÃO Cargo.Codigo = 'C4' **^** Funcionario.Cod_Cargo = Cargo.Codigo 

RESULTADO DO PRODUTO CARTESIANO 

FUNCIONARIO x CARGO 

TABELA TABELA CARGO FUNCIONARIO 

<u>Referência: Prof. Fábio Silvestre</u> 

### Passos da Execução do Produto Cartesiano com Projeção e Seleção 

Conjunto de dados processados ou que serão processados 

Conjunto de dados em processamento ou finalizado 

RESULTADO DA PROJEÇÃO **¶** Funcionario.Nome, Funcionario.Data_Admissão 

RESULTADO DA SELEÇÃO Cargo.Codigo = 'C4' **^** Funcionario.Cod_Cargo = Cargo.Codigo 

<u>Referência: Prof. Fábio Silvestre</u> 



<!-- Start of picture text -->
RESULTADO DO<br>PRODUTO<br>CARTESIANO<br>FUNCIONARIO x CARGO<br>TABELA<br>TABELA<br>CARGO<br>FUNCIONARIO<br><!-- End of picture text -->

# Operação Renomear 

**_p_ <NOVO NOME> (TABELA)** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Operação Renomear 

**Produto Cartesiano** 

¶ Cliente2.Nome, Cliente2.Rua, Cliente2.Cidade  (     Cliente2.Rua = Cliente.Rua **^** Cliente2.Cidade = Cliente.Cidade (    Nome = 'Carlos Pereira'(CLIENTE)) x ( **_q_** CLIENTE2 (CLIENTE)))) 

**Projeção** 

**Seleção Seleção** 

##### **Cliente** 

|**Codigo**|**Nome**|**Rua**|**Cidade**|
|---|---|---|---|
|1|Luis Sampaio|Rua A|Rio de Janeiro|
|2|Carlos Pereira|Rua B|Niterói|
|3|Jose Alves|Rua C|Rio de Janeiro|
|4|Luis Paulo Souza|Rua B|Niterói|



<u>Referência: Prof. Fábio Silvestre</u> 



<!-- Start of picture text -->
Passos da Execução da Operação<br>Renomear com Projeção e Seleção<br>Conjunto de dados processados ou ¶ Cliente2.Nome, Cliente2.Rua, Cliente2.Cidade<br>que serão processados<br>Conjunto de dados em processamento RESULTADO DA<br>ou finalizado PROJEÇÃO<br> Cliente2.Rua = Cliente.Rua  ^   Cliente2.Cidade = Cliente.Cidade<br>°@ RESULTADO DA<br>SELEÇÃO<br>RESULTADO DO<br>PRODUTO<br>CARTESIANO<br>CLIENTE2   x    (    Nome = 'Carlos Pereira' (CLIENTE))<br>TABELA RESULTADO DA<br>RENOMEADA SELEÇÃO<br>CLIENTE2<br>  CLIENTE2(CLIENTE)    Nome = 'Carlos Pereira' (CLIENTE)<br>Cliente CLIENTETABELA .<br>Codigo Nome Rua Cidade<br> s<br>1 Luis Sampaio Rua A Rio de Janeiro<br>a<br>2 Carlos Pereira Rua B Niterói<br>3 Jose Alves Rua C Rio de Janeiro<br>===<br>Referência: Prof. Fábio Silvestre<br>4 Luis Paulo Souza Rua B Niterói<br>se<br>q<br>q<br>q<br><!-- End of picture text -->

# Passos da Execução da Operação Renomear com Projeção e Seleção 



<!-- Start of picture text -->
Conjunto de dados processados ou ¶ Cliente2.Nome, Cliente2.Rua, Cliente2.Cidade<br>que serão processados<br>Conjunto de dados em processamento RESULTADO DA<br>ou finalizado PROJEÇÃO<br> Cliente2.Rua = Cliente.Rua  ^   Cliente2.Cidade = Cliente.Cidade<br>RESULTADO DA<br>SELEÇÃO<br>RESULTADO DO<br>PRODUTO<br>CARTESIANO<br>Cliente2 Resultado da Seleção<br>Codigo Nome Rua Cidade CLIENTE2   x    (    Nome = 'Carlos Pereira' (CLIENTE)) Codigo Nome Rua Cidade<br>1 Luis Sampaio Rua A Rio de Janeiro 2 Carlos Pereira Rua B Niterói<br>2 Carlos Pereira Rua B Niterói<br>3 Jose Alves Rua C Rio de Janeiro TABELA RESULTADO DA<br>RENOMEADA SELEÇÃO<br>CLIENTE2<br>4 Luis Paulo Souza Rua B Niterói<br>  CLIENTE2(CLIENTE)    Nome = 'Carlos Pereira' (CLIENTE)<br>TABELA<br>CLIENTE<br>q<br>q<br>q<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> ~~a~~ 

# Passos da Execução da Operação Renomear com Projeção e Seleção 

Conjunto de dados processados ou que serão processados Conjunto de dados em processamento ou finalizado 

||¶ Cliente2.Nome, Cliente2.Rua, Cliente2.Cidade|||||||
|---|---|---|---|---|---|---|---|
|RESULTADO DA<br>PROJEÇÃO|RESULTADO DA<br>SELEÇÃO<br>Cliente2.Rua = Cliente.Rua <br>**q**|**^**Cliente2.Cidade = Cliente|.Cidade|<br>**Pro**|**Resultado do**<br>**duto Cartesiano**|||
|||**Codigo**|**Nome**|**Rua**|**Cidade**|**Rua**|**Cidade**|
|||1|Luis Sampaio|Rua A|Rio de Janeiro|Rua B|Niterói|
|||2|Carlos Pereira|Rua B|Niterói|Rua B|Niterói|
||RESULTADO DO<br>PRODUTO<br>|3|Jose Alves|Rua C|Rio de Janeiro|Rua B|Niterói|
||CARTESIANO|4|Luis Paulo Souza|Rua B|Niterói|Rua B|Niterói|





<!-- Start of picture text -->
CLIENTE2   x    (    Nome = 'Carlos Pereira' (CLIENTE))<br>TABELA RESULTADO DA<br>RENOMEADA SELEÇÃO<br>CLIENTE2<br>  CLIENTE2(CLIENTE)    Nome = 'Carlos Pereira' (CLIENTE)<br>TABELA<br>CLIENTE<br>q<br>q<br><!-- End of picture text -->

<u>Referência: Prof. Fábio Silvestre</u> 

# Passos da Execução da Operação Renomear com Projeção e Seleção 

###### **Resultado da Seleção** 

|**Codigo**|**Nome**|**Rua**|**Cidade**|**Rua**|**Cidade**|
|---|---|---|---|---|---|
|2|Carlos Pereira|Rua B|Niterói|Rua B|Niterói|
|4|Luis Paulo Souza|Rua B|Niterói|Rua B|Niterói|



¶ Cliente2.Nome, Cliente2.Rua, Cliente2.Cidade 4 Luis Paulo Souza Rua B Conjunto de dados processados ou que serão processados Conjunto de dados em processamento RESULTADO DA ou finalizado PROJEÇÃO Cliente2.Rua = Cliente.Rua **^** Cliente2.Cidade = Cliente.Cidade RESULTADO DA SELEÇÃO C ~~e~~ RESULTADO DO PRODUTO CARTESIANO CLIENTE2 **x** (    Nome = 'Carlos Pereira' (CLIENTE)) ° TABELA RESULTADO DA RENOMEADA SELEÇÃO CLIENTE2 CLIENTE2(CLIENTE) Nome = 'Carlos Pereira' (CLIENTE) TABELA CLIENTE <u>Referência: Prof. Fábio Silvestre</u> ~~-~~ ~ 

# Passos da Execução da Operação Renomear com Projeção e Seleção 

**Resultado da Projeção** 

**Nome Rua Cidade** Carlos Pereira Rua B Niterói Luis Paulo Souza Rua B Niterói ~~EEE~~ ¶ Cliente2.Nome, Cliente2.Rua, Cliente2.Cidade Conjunto de dados processados ou que serão processados Conjunto de dados em processamento RESULTADO DA ou finalizado PROJEÇÃO Cliente2.Rua = Cliente.Rua **^** Cliente2.Cidade = Cliente.Cidade RESULTADO DA SELEÇÃO RESULTADO DO PRODUTO CARTESIANO CLIENTE2 **x** (    Nome = 'Carlos Pereira' (CLIENTE)) TABELA RESULTADO DA RENOMEADA SELEÇÃO *e, CLIENTE2 CLIENTE2(CLIENTE) Nome = 'Carlos Pereira' (CLIENTE) TABELA <u>Referência: Prof. Fábio Silvestre</u> CLIENTE eo? 

<u>Referência: Prof. Fábio Silvestre</u> 

# Renomear 

- RENOMEAR : ( RENOMEAR : ( ρ ) apresenta como resultado a mesma relação de apresenta, como resultado a mesma relação de entrada com outro nome ou, ainda, a mesma relação de entrada com novo nome e, também com os atributos com novos nomes. 

|<br>~~—~~|<br>  <br>| A2_ <br>|~~B2~~<br>|<br>    <br> |<sup>yvyyy{</sup><br>3333, <br>~~|~~trrr[4444|<br>|
|---|---|---|
|Referência: P<br>|rof. Fábio Silve<br>  <br>~~[Bi~~|stre<br>     <br>~~|~~KKKK[1111||



Tabelas p/ Exemplos de Operações Utilizando Teoria dos Conjuntos 

###### **Conta** 

###### **Cliente** 

|**Numero**|**Saldo**|**Cod_Agencia**|**Cod_Cliente**|
|---|---|---|---|
|256589|1200,00|1|1|
|328941|845,00|3|1|
|749621|512,00|4|3|
|856200|2650,00|2|2|
|454501|800,00|3|4|
|468952|6920,00|2|3|



|**Codigo**|**Nome**|**Rua**|**Cidade**|
|---|---|---|---|
|1|Luis Sampaio|Rua A|Rio de Janeiro|
|2|Carlos Pereira|Rua B|Niterói|
|3|Jose Alves|Rua C|Rio de Janeiro|
|4|Luis Paulo Souza|Rua B|Niterói|



###### **Emprestimo** 

|**Numero**|**Valor**|**Cod_Agencia**|**Cod_Cliente**|
|---|---|---|---|
|902230|500,00|1|1|
|902231|1500,00|3|1|
|902240|1200,00|4|2|
|902289|3000,00|2|3|
|902255|850,00|3|1|
|902299|700,00|1|3|
|902212|400,00|4|3|



<u>Referência: Prof. Fábio Silvestre</u> 

# Operação de União 

**Tabela A U Tabela B** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Operação de União 

**Produto Cartesiano** 

¶ Cliente.Nome  (     Conta.Cod_Agencia = 3 **^** Cliente.Codigo = Conta.Cod_Cliente ( CLIENTE **X** CONTA )) 

**Projeção** 

**Seleção** 

**U União** 

**Produto Cartesiano** 

¶ Cliente.Nome  (     Emprestimo.Cod_Agencia = 3 **^** Cliente.Codigo = Emprestimo.Cod_Cliente ( CLIENTE **X** EMPRESTIMO )) 

**Projeção** 

**Seleção** 

###### **Resultado da Primeira Projeção** 

**Resultado da Segunda  Projeção** 



<!-- Start of picture text -->
Nome Nome<br>Luis Sampaio Luis Sampaio<br>U<br>Luis Paulo Souza Luis Sampaio<br><!-- End of picture text -->

###### **Resultado da União** 

<u>Referência: Prof. Fábio Silvestre</u> 



<!-- Start of picture text -->
Nome<br>Luis Sampaio<br>Luis Paulo Souza<br><!-- End of picture text -->

# Operação de Intersecção 

**Tabela A Tabela B** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Operação de Intersecção 

**Produto Cartesiano** 

¶ Cliente.Nome  (     Conta.Cod_Agencia = 3 **^** Cliente.Codigo = Conta.Cod_Cliente ( CLIENTE **X** CONTA )) 

**Projeção** 

**Seleção** 

**Interseção** 

**Produto Cartesiano** 

¶ Cliente.Nome  (     Emprestimo.Cod_Agencia = 3 **^** Cliente.Codigo = Emprestimo.Cod_Cliente ( CLIENTE **X** EMPRESTIMO )) 

###### **Projeção** 

**Seleção** 

**Resultado da Primeira Projeção** 

**Resultado da Segunda  Projeção** 



<!-- Start of picture text -->
Nome Nome<br>Luis Sampaio Luis Sampaio<br>Luis Paulo Souza Luis Sampaio<br>U<br><!-- End of picture text -->

###### **Resultado da Interseção** 

<u>Referência: Prof. Fábio Silvestre</u> 

**Nome** Luis Sampaio 

# Operação de Junção 

**Tabela A |X| A.CHAVE1 = B.CHAVE2 TABELA B** 

**Junção da tabela A com a Tabela B usando como conexão entre as tabelas a Chave1 da tabela A e a chave2 da tabela B** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Operação de Junção 

**Tabela A |X| A.CHAVE1 = B.CHAVE2 TABELA B** 

**Operações Seleção e Produto Cartesiano σ A.Chave1 = B.Chave2 (A X B))** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Operação de Junção 

**CLIENTE |X| CLIENTE.CODIGO = EMPRESTIMO.COD_CLIENTE EMPRESTIMO** 

|**Codigo**|**Nome**|**Rua**|**Cidade**|**Numero**|**Valor**|**Cod_Agencia**|**Cod_Cliente**|
|---|---|---|---|---|---|---|---|
|1|Luis Sampaio|Rua A|Rio de Janeiro|902230|500,00|1|1|
|1|Luis Sampaio|Rua A|Rio de Janeiro|902255|850,00|3|1|
|1|Luis Sampaio|Rua A|Rio de Janeiro|902231|1500,00|3|1|
|2|Carlos Pereira|Rua B|Niterói|902240|1200,00|4|2|
|3|Jose Alves|Rua C|Rio de Janeiro|902289|3000,00|2|3|
|3|Jose Alves|Rua C|Rio de Janeiro|902299|700,00|1|3|
|3|Jose Alves|Rua C|Rio de Janeiro|902212|400,00|4|3|



<u>Referência: Prof. Fábio Silvestre</u> 

# Exemplo de Operação de Junção 

**Junção** 

- Cliente.Nome, Cliente.Cidade (CLIENTE |X| CLIENTE.CODIGO = EMPRESTIMO.COD_CLIENTE EMPRESTIMO) 

**Projeção** 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o modelo relacional abaixo e responda em álgebra relacional. 

   - Peca ( **<u>codigo</u>** , nome, cor, cidade) 

   - Fornecedor( **<u>codigo</u>** , nome, cidade) 

   - Fornecimento( **<u>cod_forn, cod_peca,</u>** qtde) 

   - **1) Obter o nome e a cor das peças localizadas em SP.** 

Resultado <- π nome,cor (σcidade='sp' (PECA)) 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o modelo relacional abaixo e responda em álgebra relacional. 

– Peca ( **<u>codigo</u>** , nome, cor, cidade) 

– Fornecedor( **<u>codigo</u>** , nome, cidade) 

– Fornecimento( **<u>cod_forn, cod_peca,</u>** qtde) 

- **2) Obter o código dos fornecedores que fizeram fornecimento de peça P2 com qtde maior que 200.** 

Resultado <- π cod_forn (σcod_peca='p2' ^ qtde > 200 (FORNECIMENTO)) 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o modelo relacional abaixo e responda em álgebra relacional. 

   - Peca ( **<u>codigo</u>** , nome, cor, cidade) 

   - Fornecedor( **<u>codigo</u>** , nome, cidade) 

   - Fornecimento( **<u>cod_forn, cod_peca,</u>** qtde) 

   - **3) Obter o código e o nome das peças que são vermelhas ou que tem fornecimento feito pelo fornecedor de código S1.** 

R1 <- π codigo,nome (σcor='vermelho‘ (PECA )) 

_ R2 <- π codigo,nome (σcod_forn='s1' ^ codigo=cod_peca ( PECA X FORNECIMENTO)) Les Resultado <- R1 U R2 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o modelo relacional abaixo e responda em álgebra relacional. 

   - Peca ( **<u>codigo</u>** , nome, cor, cidade) 

– Fornecedor( **<u>codigo</u>** , nome, cidade) 

- Fornecimento( **<u>cod_forn, cod_peca,</u>** qtde) 

- **4) Obter o código dos fornecedores que não fornecem a peça de código P3.** 

Resultado <- π codigo(FORNECEDOR) - π cod_forn (σcod_peca='p3'(FORNECIMENTO)) 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o modelo relacional abaixo e responda em álgebra relacional. 

   - Peca ( **<u>codigo</u>** , nome, cor, cidade) 

   - Fornecedor( **<u>codigo</u>** , nome, cidade) 

   - Fornecimento( **<u>cod_forn, cod_peca,</u>** qtde) 

**5) Obter o nome das peças fornecidas pelo fornecedor Silva.** 

R1 <- σcod_forn=codigo ^ nome='silva' ( FORNECEDOR X FORNECIMENTO)) _ R2 <- π cod_peca (R1) Les Resultado <- π nome (σcod_peca=codigo (PECA X R2)) 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o modelo relacional abaixo e responda em álgebra relacional. 

   - Peca ( **<u>codigo</u>** , nome, cor, cidade) 

   - Fornecedor( **<u>codigo</u>** , nome, cidade) 

   - Fornecimento( **<u>cod_forn, cod_peca,</u>** qtde) 

**6) Recuperar o nome das peças que tiveram fornecimento.** 

R1 <- σcodigo=cod_peca ( PECA X FORNECIMENTO) _ Resultado <- π nome ( R1) 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o BD relacional. Dê uma expressão em álgebra relacional para cada uma das consultas abaixo: 

      - reside (pessoa_nome, rua, cidade) 

      - trabalha (pessoa_nome, empresa_nome, salário) 

      - localizado (empresa_nome, cidade) 

      - gerencia (pessoa_nome, gerente_nome) 

      - **1) Encontre o nome de todos os funcionários que trabalham para a empresa Vai-bem** 

   - π pessoa_nome (σ empresa_nome = “Vai-bem” (trabalha)) 

<u>Referência: Prof. Fábio Silvestre</u> ~~ae~~ 

# Exercícios 

- Considere o BD relacional. Dê uma expressão em álgebra relacional para cada uma das consultas abaixo: 

   - reside (pessoa_nome, rua, cidade) 

   - trabalha (pessoa_nome, empresa_nome, salário) 

   - localizado (empresa_nome, cidade) 

   - gerencia (pessoa_nome, gerente_nome) 

   - **2) Encontre o nome e a cidade de todos os funcionários que trabalham para a Leva-tudo** 

π pessoa_nome, cidade (σ trabalha.pessoa_nome = reside.pessoa_nome ^empresa_nome = “Leva-tudo” (trabalha × reside)) 

<u>Referência: Prof. Fábio Silvestre</u> 

# Exercícios 

- Considere o BD relacional. Dê uma expressão em álgebra relacional para cada uma das consultas abaixo: 

   - reside (pessoa_nome, rua, cidade) 

   - trabalha (pessoa_nome, empresa_nome, salário) 

   - localizado (empresa_nome, cidade) 

   - gerencia (pessoa_nome, gerente_nome) 

   - **3) Encontre todos os empregados que não trabalham para a Vai-bem** 

σ empresa_nome <> “Vai-bem” (trabalha) 

<u>Referência: Prof. Fábio Silvestre</u> ~~ae~~ 

# Exercícios 

- Considere o BD relacional. Dê uma expressão em álgebra relacional para cada uma das consultas abaixo: 

   - reside (pessoa_nome, rua, cidade) 

   - trabalha (pessoa_nome, empresa_nome, salário) 

   - localizado (empresa_nome, cidade) 

   - gerencia (pessoa_nome, gerente_nome) 

   - **4) Encontre o nome, rua e cidade de todos os funcionários que trabalham para a Leva-tudo e recebem mais de R$ 2.000,00.** 

π pessoa_nome, rua, cidade (σ trabalha.pessoa_nome = reside.pessoa_nome ∧ empresa_nome = “Leva-tudo” ∧ al trabalha.salário > 2000 (trabalha × reside)) 

<u>Referência: Prof. Fábio Silvestre</u> ~~ae~~ 

# Exercícios 

- Considere o BD relacional. Dê uma expressão em álgebra relacional para cada uma das consultas abaixo: 

   - reside (pessoa_nome, rua, cidade) 

   - trabalha (pessoa_nome, empresa_nome, salário) 

   - localizado (empresa_nome, cidade) 

   - gerencia (pessoa_nome, gerente_nome) 

   - **5) Encontre o nome de todas as pessoas que trabalham nas empresas que situam-se em Cianorte.** 

π trabalha.pessoa_nome (σ trabalha.empresa_nome = reside.empresa_nome  ^ localizado.cidade = “Cianorte” (localizado × trabalha)) al 

<u>Referência: Prof. Fábio Silvestre</u> ~~ae~~ 

