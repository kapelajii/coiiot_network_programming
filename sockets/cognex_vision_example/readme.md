# Socket example (Cognex machine vision TELNET interface)

<img src="abb_cognex_communication.png">


> The In-Sight Native Mode protocol is an ASCII protocol that allows an In-Sight sensor to be controlled from any of the following:

> - Custom application programs running on a PC
> - Remote hosts that support standard serial communications
> - **Telnet over an Ethernet network**

> The Native Mode protocol is divided into two sets of commands: Basic and Extended.
> - Basic Native Mode commands are two characters long, plus parameters (if any) and a terminator character.
> - Extended Native Mode commands include additional functions or commands.
> The commands are not case sensitive. The terminator is CR + LF (ASCII characters 13 + 10) when sending Native Mode commands using a telnet connection. When using Native > Mode commands over a serial port, an alternate terminator character may be specified in the Native Mode Details.
> The default terminator is CR (ASCII character 13).

> When a Native Mode command is remotely issued to an In-Sight sensor, the In-Sight sensor processes the command and then returns a response, consisting of an ASCII > string followed by the terminator character.

> Commands that set values return **1 for "success"** , **0 for "unrecognized command"**, or a **negative number for "failure"**.
> Commands that get values return various values, depending on the command.

Source: [Cognex cocumentation - Native mode commands](https://support.cognex.com/docs/is_613/web/EN/ise/Content/Communications_Reference/NativeMode_Commands.htm?tocpath=Communication%20Reference%7CNative%20Mode%20Communications%7C_____1)


## Excersice 1. Telnet client to read data from machine vision camera

In this excersice we desing socket client (Telnet) wich can trigger camera and read position data.
Camera is connected to robot and robot needs part x, y coordiantes and orientation to locate part for picking using machine vision.
In this example data is stored in spreadsheet cell C7 inside Cognex insight explorer Spreadsheet View. 

Implement socket application that creates a socket connection,  send a message to the socket (take a picture) validates the response from the socket and then reads the values from cell C7 of the spreadsheet if earlier request  success.

**Cognex simulator**

(file: cognex_simulator.py)

IP address: 127.0.0.1

PORT: 10001

data format: "x-coordinate, y-coordinate, orientation"

**1. What is command and parameter to Acquire an image and update the spreadsheet?**

Read documentation below 👇

[Cognex documentation- Set event and wait](https://support.cognex.com/docs/is_613/web/EN/ise/Content/Communications_Reference/SetEventAndWait.htm)

<details>
<summary>Answer</summary>

```
SW8
```
</details>


**2. What is command and parameter to read value from spreadsheet cell c7?**

Read documentation below 👇

[Cognex documentation - Get value from spreadsheet](https://support.cognex.com/docs/is_613/web/EN/ise/Content/Communications_Reference/GetValue_Spreadsheet.htm)

<details>
<summary>Answer</summary>

```
GVC007
```
</details>

**3. What is return value from server if Acquire an image command succeed?**

<details>
<summary>Answer</summary>

```
1
```
</details>






