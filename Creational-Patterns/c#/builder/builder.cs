/*
Type: Creational

*When use it?

*You want to construct a complex object step by step, separating its construction from its representation.
*You want to produce different types or representations of an object using the same construction process.

Common use cases

*Constructing meal combos in a fast-food system.
*Constructing detailed documents or HTML representations.
*Assembling intricate 3D models in graphics software.
*Building complex data payloads for communication protocols.

*/

public class Computer
{
    public string Cpu { get; set; }
    public string Ram { get; set; }
    public string Storage { get; set; }
    public string GraphicsCard { get; set; }

    public void DisplayComputerInfo()
    {
        Console.WriteLine("Computer Info: ");
        Console.WriteLine($"Head: {Cpu} ");
        Console.WriteLine($"Ram: {Ram} ");
        Console.WriteLine($"Storage: {Storage} ");
        Console.WriteLine($"GraphicsCard: {GraphicsCard} ");
    }
}

public class ComputerBuilder : IComputerBuilder
{
    private Computer _computer = new Computer();

    public void BuildCpu(string cpu)
    {
        _computer.Cpu = cpu;
    }
    public void BuildRam(string ram)
    {
        _computer.Ram = ram;
    }
    public void BuildStorage(string storage)
    {
        _computer.Storage = storage;
    }
    public void BuildGraphicsCard(string graphicsCard)
    {
        _computer.GraphicsCard = graphicsCard;
    }

    public Computer GetComputer()
    {
        return _computer;
    }
}

public class ComputerDirector
{
    private IComputerBuilder _computerBuilder;

    public ComputerDirector(IComputerBuilder computerBuilder)
    {
        _computerBuilder = computerBuilder;
    }

    public void ConstructComputer()
    {
        _computerBuilder.BuildCpu("Rizen I9");
        _computerBuilder.BuildRam("32 GB");
        _computerBuilder.BuildStorage("5TB");
        _computerBuilder.BuildGraphicsCard("RTX 3090");
    }
}

public interface IComputerBuilder
{
    void BuildCpu(string cpu);
    void BuildRam(string ram);
    void BuildStorage(string storage);
    void BuildGraphicsCard(string graphicsCard);
    Computer GetComputer();
}

IComputerBuilder computerBuilder = new ComputerBuilder();
ComputerDirector director = new ComputerDirector(computerBuilder);

director.ConstructComputer();

Computer computer = computerBuilder.GetComputer();
computer.DisplayComputerInfo();
