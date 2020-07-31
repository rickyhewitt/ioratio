## ioratio.py 
A linux utility for displaying device IO & read % / write % ratio

## Screenshot
![Screenshot](https://user-images.githubusercontent.com/1459733/88938156-e4187b80-d239-11ea-927f-88e69ec29ae1.png)

## Requirements
python3

## Example usage

### Stats for /dev/sda1
`ioratio.py /dev/sda1`

### Stats all sd* devices
`ioratio.py /dev/sd`

### Watch all sd devices every 1 sec
`watch -n1 ioratio.py /dev/sd`

## License
MIT License

## Credit
Ricky Hewitt <rickyhewitt.dev>)
