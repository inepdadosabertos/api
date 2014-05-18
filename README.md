
## **PROJETO DADOS ABERTOS DO INEP**

### Objetivos do projeto
* Mostrar que é possível disponibilizar dados do INEP seguindo as recomendações da Cartilha de Dados Abertos (http://dados.gov.br/cartilha-publicacao-dados-abertos/)
* Disponibilizar os dados mais brutos e permitir que seja feito o acesso simplificado, com considerações semânticas da URL e com identificadores únicos e persistentes

### Domínio da API

* Utilize o endereço http://api.dadosabertosinep.org/v1 como prefixo de todas as chamadas dessa API


### URLs de chamadas da API

**Retorna escolas com um determinado filtro (não exclusivo) [micro-dado]**
   * /ideb/escolas.{json}
   
     * Paramêtros (pelo menos um parâmetro deve ser informado)
      * uf=[sigla]
      * codigo_municipio=[cod_municipio]
      * rede=[municipal|estadual|federal|publica]
   
     * Exemplos
      * http://api.dadosabertosinep.org/v1/ideb/escolas.json?uf=RR 
      * http://api.dadosabertosinep.org/v1/ideb/escolas.json?uf=RR&rede=estadual
      * http://api.dadosabertosinep.org/v1/ideb/escolas.json?codigo_municipio=1100254
      * http://api.dadosabertosinep.org/v1/ideb/escolas.json?codigo_municipio=1100254&rede=municipal

**Retorna resumo dos dados de um determinado filtro (não exclusivo)**
   * /ideb.{json}
 
     * Paramêtros
      * uf=[sigla] obrigatório
  
     * Exemplo
      * http://api.dadosabertosinep.org/v1/ideb.json?uf=ES

**Retorna uma escola específica**
   * /ideb/escola/[código_escola].{json}
  
     * Exemplo
      * http://api.dadosabertosinep.org/v1/ideb/uf/[uf].{json|cvs}  

**(FUTURO) retorna resumo agrupado de uma UF específica**
   * /ideb/uf/[uf].{json}
  
     * Paramêtros
      * rede=[municipal|estadual|federal|publica]
  
     * Exemplos
      * http://api.dadosabertosinep.org/v1/ideb/uf/MG.json
      * http://api.dadosabertosinep.org/v1/ideb/uf/MG.json?rede=municipal

**(FUTURO) retorna resultado agrupado de um município específico**
  * /ideb/municipio/[código_municipio].{json}
     
     * Exemplo
      * http://api.dadosabertosinep.org/v1/ideb/municipio/1100254.json

### Roadmap do projeto

1. refinar a lógica de organização dos dados

  1. Criar “bucket único das escolas” agrupando dados das escolas dos censos (educação básica e ensino superior) com as informações únicas das escolas (inclusive dados de geolocalização)
  1. Criar “bucket do censo escolar” com os dados de estrutura, cursos, docentes e alunos
  1. Criar “bucket de cada indicador” com o código da escola como chave. Exemplo: bucket “ideb”, com a chave “11046430” ([código_escola]_[indicador]) e nesse índice exibir os dados agrupados por ano
  1. Estudar e identificar modelo de buckets para as pesquisas (SAEB, ENEM, PADAE, PNERA, PROVAO, PROVA BRASIL, CENSO MAGISTERIO)

2. gerar visualizações dos dados brutos nos formatos csv, html e xml como ocorre no http://api.convenios.gov.br/


