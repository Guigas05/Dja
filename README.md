### Projeto de Receitas com Django

Este projeto de receitas foi desenvolvido como parte de um curso de Django, um dos frameworks mais populares para desenvolvimento web em Python. A aplicação permite o gerenciamento de receitas, onde os usuários podem criar, visualizar e atualizar suas próprias receitas. O projeto faz uso de diversos recursos nativos do Django, incluindo o sistema de modelos, templates, e o uso de URLs.

#### Estrutura Geral do Projeto

O projeto é organizado de maneira típica para um aplicativo Django. Abaixo estão os principais diretórios e arquivos que compõem o projeto, conforme exibido na imagem fornecida:

- **migrations/**: Diretório contendo as migrações de banco de dados, geradas automaticamente pelo Django para refletir as mudanças no modelo de dados.
- **static/recipes/css/**: Diretório para armazenar arquivos CSS específicos da aplicação de receitas.
- **templates/recipes/**: Diretório contendo os templates HTML para renderização das páginas da aplicação.
- **tests/**: Contém os testes unitários da aplicação.
- **admin.py**: Configurações para o painel administrativo do Django.
- **apps.py**: Configurações específicas do aplicativo dentro do projeto Django.
- **models.py**: Definição dos modelos de dados da aplicação (detalhado abaixo).
- **urls.py**: Mapeamento de URLs para as views correspondentes.
- **views.py**: Contém as funções e classes que manipulam as requisições HTTP e retornam as respostas.

### Modelos

Os modelos são a representação das tabelas do banco de dados na aplicação Django. Eles utilizam classes Python que herdam de `models.Model`. No contexto deste projeto de receitas, temos dois modelos principais: **Category** e **Recipe**.

#### Category (Categoria)

A classe `Category` representa as categorias às quais as receitas podem ser associadas. Cada categoria contém apenas um campo `name`, que é o nome da categoria.

```python
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
```

- **name**: Um campo de texto com comprimento máximo de 65 caracteres para armazenar o nome da categoria.
- **__str__**: Método que retorna o nome da categoria quando o objeto é convertido para string.

#### Recipe (Receita)

A classe `Recipe` representa as receitas em si, contendo informações detalhadas como título, descrição, tempo de preparo, unidades de medida, e muito mais.

```python
class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
```

##### Campos

- **title**: Título da receita, um campo de texto com no máximo 65 caracteres.
- **description**: Uma breve descrição da receita, com até 165 caracteres.
- **slug**: Campo do tipo `SlugField`, utilizado para criar URLs amigáveis baseadas no título da receita.
- **preparation_time**: Um campo do tipo inteiro para armazenar o tempo de preparo.
- **preparation_time_unit**: Unidade de medida para o tempo de preparo (por exemplo, "minutos", "horas").
- **servings**: Campo para o número de porções.
- **servings_unit**: Unidade de medida para as porções (por exemplo, "pessoas", "fatias").
- **preparation_steps**: Campo de texto extenso onde os passos da receita são descritos.
- **preparation_steps_is_html**: Um campo booleano que indica se os passos da receita estão formatados como HTML.
- **created_at**: Armazena a data e hora em que a receita foi criada, preenchido automaticamente quando a receita é adicionada.
- **updated_at**: Atualizado automaticamente sempre que a receita é editada.
- **is_published**: Um campo booleano que indica se a receita foi publicada.
- **cover**: Um campo de imagem que permite o upload de uma imagem de capa para a receita, organizada em subdiretórios por ano, mês e dia.
- **category**: Um campo `ForeignKey` que relaciona a receita com uma categoria, permitindo que seja nula.
- **author**: Um campo `ForeignKey` que relaciona a receita a um autor (usuário), também podendo ser nulo.

##### Métodos

- **__str__**: Retorna o título da receita como a representação de string do objeto.

### Funcionalidades do Projeto

1. **Sistema de Categorias**: As receitas podem ser classificadas em diferentes categorias.
2. **Upload de Imagens**: O projeto permite o upload de uma imagem de capa para cada receita, que é armazenada de forma organizada por ano, mês e dia.
3. **Controle de Publicação**: Apenas receitas que são marcadas como publicadas (`is_published=True`) serão exibidas publicamente.
4. **Relacionamento com Usuários**: As receitas são associadas a usuários (autores), facilitando o controle de quais receitas pertencem a quais usuários.

### Próximos Passos a seren desenvolvidos

1. **Comentários e Avaliações**: Implementar um sistema onde os usuários possam comentar e avaliar as receitas.
2. **Busca e Filtros**: Adicionar funcionalidades de busca e filtros por categorias, tempo de preparo, ou porções.
3. **Sistema de Favoritos**: Permitir que os usuários marquem receitas como favoritas.
4. **Integração com API**: Criar uma API para o projeto utilizando o Django Rest Framework, permitindo que as receitas sejam acessadas via uma interface de API.
