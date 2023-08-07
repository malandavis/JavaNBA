javac .\src\Main.java
Set-Location .\src
java Main

## Clears class files that were generated in the src folder
Remove-Item *.class


## Back to original directory
Set-Location ..