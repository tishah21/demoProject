import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AuthServiceService } from '../services/auth-service.service';
// import {MatIconModule} from '@angular/material/icon';
// import {MatDividerModule} from '@angular/material/divider';
// import {MatButtonModule} from '@angular/material/button';
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  data: any;
  constructor(private authService: AuthServiceService) { }

  onClick() {
    console.log("Login Works");
    this.authService.getAll().subscribe({
      next: (data) => {
        debugger;
        this.data = JSON.stringify(data);
        console.log(data);
      },
      error: (e) => console.error(e)
    })
  }
}
