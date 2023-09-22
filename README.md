# SOLID (Object-Oriented Programming Principles)

- Acrônimo criado por Michael Feathers à partir dos princípios da orientação a objetos e design de código criados por Robert C. Martin (a.k.a. Uncle Bob).

1. S - `SRP` - Single Responsiblity Principle (Princípio da Responsabilidade Única)
2. O - `OCP` - Open-Closed Principle (Princípio Aberto-Fechado)
3. L - `LSP` - Liskov Substitution Principle (Princípio da Substituição de Liskov)
4. I - `ISP` - Interface Segregation Principle (Princípio da Segregação da Interface)
5. D - `DIP` - Dependency Inversion Principle (Princípio da Inversão da Dependência)

# Conceitos: Interface e Classe Abstrata

* Ferramentas para Desacoplar (Segregar) Implementação (Código) e Assinatura (Tipo de Retorno, Nome e Parâmetros) de Métodos (Facilita Manutenção do Código)

- `Interface` (implements): é uma entidade (objeto), que não pode ser instanciada, e que especifica um conjunto de métodos abstratos (somente abstratos) que um grupo de classes deverá, obrigatoriamente, implementar. Método abstrato é um tipo de método especial que não possui implementação, apenas assinatura, e obriga as classes herdeiras a implementar estes métodos. Uma classe pode herdar diversas interfaces, mas criar novos métodos nesta classe não é interessante, pois será obrigatório implementar os novos métodos em todas as classes derivadas.

- `Classe Abstrata` (extends): é um tipo de classe especial que não pode ser instanciada (criar objeto à partir dela), apenas herdada (como uma super classe). Armazena atributos e métodos (obrigatório pelo menos um método abstrato) comuns às classes que a irão herdar, permitindo um maior reaproveitamento de código. Uma classe pode herdar de somente uma classe abstrata, mas é possível criar novos métodos na classe herdeira.

- Comum: Classe Concreta `extends` Classe Abstrata `implements` Interface

- Sempre que precisarmos definir um conjunto de métodos que devem ser obrigatoriamente implementados por um grupo de classes concretas, utilizamos as interfaces. Se houver a necessidade de implementar algum método adicional específico para determinada classe concreta, utilizamos as classes abstratas.

# Conceitos: Interface e Classe Abstrata em Python

- Python (assim como JavaScript, Ruby, PHP) é uma linguagem dinâmica.
- Python não possui uma keyword interface, como outras linguagens (Java, Go, C++).
- Python não obriga que todos os métodos abstratos da interface sejam implementados pela classe concreta (herdeira).

- Uma interface é reconhecida em Python através de Duck Typing.
- Duck Typing (if it walks like a duck, and it quacks like a duck, then it must be a duck): é um estilo de codificação de linguagens dinâmicas onde o tipo da variável não importa, contando que seu comportamento (métodos) seja o desejado.

- numa linguagem estática, a interface é utilizada como um contrato, ou seja, a classe concreta que deseja implementar esta interface deve seguir todos os métodos e atributos (obrigatórios) e o objeto recebido deve ser do tipo determinado, para que se tenha o comportamento esperado.
- numa linguagem dinâmica, utiliza-se a prática EAFP (Easier to Ask for Forgiveness than Permission) para prevenir problemas como executar um método que não existe em um objeto. É um estilo de codificação que envolve assumir que os comportamentos desejados em um determinado objeto existem e qualquer problema relacionado é tratado como uma exceção.

# Conceitos: args e kwargs em Python

*args (arguments): argumentos não nomeados
*args é usado para receber uma lista de argumentos de comprimento variável sem a palavra-chave (keyword) na função.

**kwargs (keyword arguments): argumentos nomeados
Eles estarão disponíveis como um dicionário ({'chave': 'valor'}) dentro da função.

- permitem que se passe um número não especificado de argumentos para uma função.
- por concenção se utiliza *args e **kwargs, mas podem ter qqr nome.
- na chamada da função, argumentos não nomeados (*args) devem sempre vir antes dos argumentos nomeados (**kwargs).

Informal Interface
FOrmal Interface


# Principles

1. `SRP` - Single Responsiblity Principle

- Uma classe deve ser especializada em um único assunto e possuir apenas uma responsabilidade dentro do software, ou seja, uma única tarefa ou ação para executar.
- Uma classe que sabe demais ou faz demais (God Class) não é uma boa prática, dificulta manutenção do código.

* Problemas da violação do SRP:

- Falta de coesão;
- Alto acoplamento (maior nível de dependências -> sistema engessado e frágil para alterações);
- Dificuldades na implementação de testes automatizados (difícil “mockar” esse tipo de classe);
- Dificuldades para reaproveitar o código.

2. `OCP` - Open-Closed Principle

- objetos (entidades) devem estar abertos para extensão, mas fechados para modificação, ou seja, quando novos comportamentos (métodos) e recursos (propriedades) precisam ser adicionados ao software, devemos estender e não alterar o código fonte original.

- formas de extensão: interface, mix-in


- mix-in é uma classe que não se destina a ser independente - existe para adicionar funcionalidade extra a outra classe através de herança múltipla.
- No Python não existe uma maneira específica de criar mix-ins. Os programadores, por convenção e para deixar explícito a classe como um mix-in, colocam o termo 'MixIn' no nome da classe e utilizam através de herança múltipla.




# Conceitos

- Framework: programa, conjunto de programas e/ou biblioteca que escreve a maior parte do código para a gente.