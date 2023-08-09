javac .\src\*.java
Set-Location .\src
java Main 1

## Clears class files that were generated in the src folder
Remove-Item *.class


## Back to original directory
Set-Location ..