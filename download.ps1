$FolderMyDocuments = [environment]::getfolderpath("mydocuments")
$OutFilePath = [io.path]::combine($FolderMyDocuments, 'My Games', 'Path of Exile', 'ganymede.filter')
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/wiredbomb0/valkyrie/master/ganymede.filter" -OutFile $OutFilePath
