export default function registerForm() {


  return (
          // Register form desktop layout 
          <div className="grid grid-cols-2 card p-2 items-center justify-cente w-1/2 shadow-lg border rounded-lg">
            <div className="col-span-2 text-center items-center">
              <h2 className="card-title">Register</h2>
            </div>

            <div className="mb-2 mr-2">
              <label className="">
                Username
                <input type="text" className="input input-sm m-1" placeholder="Username" />
              </label>
            </div>
            
            <div className="mb-2 mr-2">
              <label className="">
                Email
                <input type="text" className="input input-sm m-1" placeholder="daisy@site.com" />
              </label>
            </div>
            

            <div className="mb-2 mr-2">
              <label className="">
                Password: 
                <input type="password" className="input input-sm m-1" placeholder="Enter password" />
              </label>
            </div>
            

            <div className="mb-2 mr-2">
              <label className="">
                Confirm Password: 
                <input type="password" className="input input-sm m-1" placeholder="Confirm password" />
              </label>
            </div>

            <div className="col-span-2 grid grid-cols-2">
              <button className="btn btn-outline btn-neutral btn-sm m-2 hover:scale-95">Register</button>
              <button className="btn btn-outline btn-neutral btn-sm m-2 hover:scale-95">Cancel</button>
            </div>
            
          </div>
          
  );
}



