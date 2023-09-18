# SOLID (Object-Oriented Programming Principles)

- acrônimo criado por Michael Feathers à partir dos princípios da orientação a objetos e design de código criados por Robert C. Martin (a.k.a. Uncle Bob).

1. S - `SRP` - Single Responsiblity Principle (Princípio da Responsabilidade Única)
2. O - `OCP` - Open-Closed Principle (Princípio Aberto-Fechado)
3. L - `LSP` - Liskov Substitution Principle (Princípio da Substituição de Liskov)
4. I - `ISP` - Interface Segregation Principle (Princípio da Segregação da Interface)
5. D - `DIP` - Dependency Inversion Principle (Princípio da Inversão da Dependência)

# Conceitos Básicos

* Ferramentas para Desacoplar (Segregar) Implementação e Assinatura de Métodos (Facilita Manutenção do Código)

- `Interface` (implement): é uma entidade (objeto), que não pode ser instanciada, e que especifica um conjunto de métodos abstratos (somente abstratos) que um grupo de classes deverá, obrigatoriamente, implementar. Método abstrato é um tipo de método especial que não possui implementação (código), apenas assinatura (tipo de retorno, nome e parâmetros), e obriga as classes herdeiras a implementar estes métodos. Uma classe pode herdar diversas interfaces, mas criar novos métodos nesta classe não é interessante, pois será obrigatório implementar os novos métodos em todas as classes derivadas.

- `Classe Abstrata` (extends): é um tipo de classe especial que não pode ser instanciada (criar objeto à partir dela), apenas herdada (como uma super classe). Armazena atributos e métodos (pelo menos um método abstrato e demais não-abstratos) comuns às classes que a irão herdar, permitindo um maior reaproveitamento de código. Uma classe pode herdar de somente uma classe abstrata, mas é possível criar novos métodos na classe herdeira.

- Comum: Classe Concreta `extends` Classe Abstrata `implements` Interface

- Sempre que precisarmos definir um conjunto de métodos que devem ser obrigatoriamente implementados por um grupo de classes, utilizamos as interfaces. Se houver a necessidade de implementar algum método adicional específico para determinada classe, utilizamos as classes abstratas.

# Principles

1. `SRP` - Single Responsiblity Principle

- uma classe deve ser especializada em um único assunto e possuir apenas uma responsabilidade dentro do software, ou seja, uma única tarefa ou ação para executar.
- uma classe que sabe demais ou faz demais (God Class) não é uma boa prática, dificulta manutenção do código.

2. `OCP` - Open-Closed Principle

- objetos (entidades) devem estar abertos para extensão, mas fechados para modificação, ou seja, quando novos comportamentos (métodos) e recursos (propriedades) precisam ser adicionados ao software, devemos estender e não alterar o código fonte original.

- formas de extensão: interface, mix-in

-  interface é uma maneira de declarar o comportamento de uma classe em outra, permitindo com que esta e outras classes acessem este comportamento através de herança.
- mix-in é uma classe que não se destina a ser independente - existe para adicionar funcionalidade extra a outra classe através de herança múltipla.
- No Python não existe uma maneira específica de criar mix-ins. Os programadores, por convenção e para deixar explícito a classe como um mix-in, colocam o termo 'MixIn' no nome da classe e utilizam através de herança múltipla.
- classe abstrata é um tipo de classe especial que não pode ser instanciada, apenas herdada. Sendo assim, uma classe abstrata não pode ter um objeto criado a partir de sua instanciação. Essas classes são 



# Conceitos

- Framework: programa, conjunto de programas e/ou biblioteca que escreve a maior parte do código para a gente.