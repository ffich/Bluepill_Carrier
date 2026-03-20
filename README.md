# BluePill Experimental Carrier

🧪 **BluePill Experimental Carrier** is a carrier board designed for development, testing, and rapid experimentation with the **STM32 Blue Pill (STM32F103)**.

The goal of this board is to provide a **feature-rich development platform** with integrated peripherals, industrial communication interfaces, and expansion sockets, while keeping the design clean, educational, and easy to extend.

---

## ✨ Key Features

### On-board Peripherals
- 14 × Status / debug LEDs  
- 3 × User buttons  
- 1 × Wake-up button  
- 1 × Analog potentiometer  
- **TMP102** I2C temperature sensor  
- **I²C OLED** display  
- **SPI EEPROM**  


### Communications
- **CAN bus TJA1051T3** transceiver
- **LIN Bus TJA1029T** transceiver (Configurable Master/Slave)
- **RS-485** interface with dedicated transceiver
- **USB / Serial** interface

### Security
- **Microchip ATECC608C** Cryptographic coprocessor

### Expansion Sockets
- External **DS3231 RTC Breakout** socket  
- **BME280** environmental sensor socket  

<img width="811" height="689" alt="image" src="https://github.com/user-attachments/assets/300a8b3b-801f-46ca-8db9-fd5a6e5ec751" />

---

## 🎯 Design Philosophy

- Built for **experimentation, prototyping, and hardware/software testing**
- Well suited for:
  - Embedded development
  - Industrial and automotive communications (CAN, LIN, RS-485)
  - Sensor integration
  - Industrial and IoT applications
  - Cybersecurity

---

## 🧩 Target Audience

- Advanced makers  
- Electronics / embedded students  
- STM32 firmware developers  
- Educational labs and R&D teams  

---

## ⚠️ Disclaimer

This board is **experimental by design**.  
Layout, features, and routing may evolve as the project progresses and new tests are performed.

---

## 📜 License

Hardware and documentation are released under an open-source license.  
See the `LICENSE` file for details.

