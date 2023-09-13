/*
Type: Creational

*When to use it?

*You want to ensure a single instance of a class throughout an application's lifecycle.
*You desire a global access point to that instance.

Common use cases:

*Managing unique connections (like to databases).
*Logging systems.
*Global settings or configurations.
*Data caching.

*/

public class Singleton
{
    // Declares and initializes a static, read-only instance of the Singleton class.
    // Since this is static, it will be created only once, when the class is first accessed.
    private static readonly Singleton _instance = new Singleton();

    // Private constructor ensures that no other instance of this class can be created directly 
    // using the 'new' keyword from outside of this class.
    private Singleton()
    {

    }

    public static Singleton Instance
    {
        get
        {
            return _instance;
        }
    }
}

Singleton singleton = Singleton.Instance;
